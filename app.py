import streamlit as st
import cv2, os, time, tempfile
import numpy as np
from collections import deque
from ultralytics import YOLO
import torch

# ================== SAYFA ==================
st.set_page_config(page_title="PPE Tespiti — CUDA Hızlı ve Stabil", layout="wide")
st.title("🦺 PPE Tespiti — Gerçek Zaman Kutular + Doğru Eşleştirme")

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ================== CİHAZ ==================
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
HALF   = True if DEVICE.startswith("cuda") else False   # FP16 sadece GPU'da
IMG_SIZE = 640

st.caption(f"🖥️ Cihaz: **{DEVICE}**  •  FP16: **{HALF}**  •  imgsz={IMG_SIZE}")

# ================== MODELLER ==================
@st.cache_resource
def load_models():
    human = YOLO("insantespit.pt")  # İnsan
    ppe   = YOLO("best.pt")       # Baret + Yelek
    return human, ppe

human_model, ppe_model = load_models()

# ================== SOL PANEL ==================
with st.sidebar:
    st.header("⚙️ Tespit Eşikleri")
    HUMAN_TH   = st.slider("İnsan eşiği", 0.1, 0.9, 0.35, 0.05)
    HELMET_TH  = st.slider("Baret eşiği", 0.1, 0.9, 0.35, 0.05)
    VEST_TH    = st.slider("Yelek eşiği", 0.1, 0.9, 0.35, 0.05)

    st.header("🛡️ Güven Kuralları")
    MIN_H_CONF = st.slider("Min baret güveni", 0.1, 0.95, 0.70, 0.05)
    MIN_V_CONF = st.slider("Min yelek güveni", 0.1, 0.95, 0.70, 0.05)
    IOU_MIN    = st.slider("Min IoU (kişi↔PPE)", 0.0, 0.4, 0.05, 0.01)

    st.header("🎬 Oynatma")
    KEEP_SOURCE_FPS = st.checkbox("Kaydı kaynak FPS'te yap", True)

    SHOW_DEBUG = st.checkbox("Baş/Gövde hatlarını ve PPE merkezlerini çiz (debug)", False)

# ================== YARDIMCI ==================
def enhance(img):
    # Hız + tutarlılık için sabit boyut
    return cv2.resize(img, (1280, 720))

def norm_label(s: str) -> str:
    s = str(s).lower()
    if any(w in s for w in ["person", "people", "insan", "human"]): return "person"
    if any(w in s for w in ["helmet", "hardhat", "baret", "safety_helmet"]): return "helmet"
    if any(w in s for w in ["vest", "reflective_jacket", "safety_vest", "yelek", "jacket"]): return "vest"
    return s

def parse(results, names, wanted_set, th):
    out=[]
    for b in results.boxes:
        conf=float(b.conf[0]); 
        if conf < th: 
            continue
        c=int(b.cls[0])
        lbl = norm_label(names[c] if isinstance(names, dict) else names[c])
        if lbl in wanted_set:
            x1,y1,x2,y2 = map(int, b.xyxy[0])
            out.append({"box":(x1,y1,x2,y2), "conf":conf, "label":lbl})
    return out

def center_of(box):
    x1,y1,x2,y2 = box
    return ( (x1+x2)//2, (y1+y2)//2 )

def fast_iou(a,b):
    x1=max(a[0],b[0]); y1=max(a[1],b[1])
    x2=min(a[2],b[2]); y2=min(a[3],b[3])
    inter = max(0,x2-x1)*max(0,y2-y1)
    if inter<=0: return 0.0
    areaA=(a[2]-a[0])*(a[3]-a[1])
    areaB=(b[2]-b[0])*(b[3]-b[1])
    return inter / float(areaA+areaB-inter)

# Baş (üst %45), gövde (%20–95) kuralı + IoU eşleştirme (greedy 1–1) + yedek kural
def assign(persons, helmets, vests, iou_min, min_h, min_v, debug_img=None, show_debug=False):
    def head_torso_limits(pbox):
        x1,y1,x2,y2 = pbox; h=y2-y1
        head_max  = y1 + int(0.45*h)
        torso_top = y1 + int(0.20*h)
        torso_bot = y1 + int(0.95*h)
        return head_max, torso_top, torso_bot

    people=[]
    for i,p in enumerate(persons):
        pb=p["box"]; pc=center_of(pb)
        head_max, torso_top, torso_bot = head_torso_limits(pb)
        people.append((i,pb,pc,head_max,torso_top,torso_bot))

    if show_debug and debug_img is not None:
        for _,pb,_,head_max,torso_top,torso_bot in people:
            x1,y1,x2,y2=pb
            cv2.line(debug_img,(x1,head_max),(x2,head_max),(255,255,0),2)
            cv2.line(debug_img,(x1,torso_top),(x2,torso_top),(0,255,255),2)
            cv2.line(debug_img,(x1,torso_bot),(x2,torso_bot),(0,255,255),2)
        for h in helmets:
            cx,cy=center_of(h["box"]); cv2.circle(debug_img,(cx,cy),4,(255,0,0),-1)
        for v in vests:
            cx,cy=center_of(v["box"]); cv2.circle(debug_img,(cx,cy),4,(0,255,255),-1)

    def match(ppe_list, kind):
        # (mesafe, person_idx, ppe_idx)
        pairs=[]
        for pi,pb,pc,head_max,torso_top,torso_bot in people:
            for ji,obj in enumerate(ppe_list):
                ob=obj["box"]; oc=center_of(ob)
                # PPE merkezi kişi kutusu içinde mi?
                if not (pb[0] <= oc[0] <= pb[2] and pb[1] <= oc[1] <= pb[3]):
                    continue
                iou = fast_iou(pb, ob)
                if kind=="helmet":
                    if not (pb[1] <= oc[1] <= head_max): continue
                    if iou < iou_min: continue
                else:  # vest
                    if not (torso_top <= oc[1] <= torso_bot): continue
                    if iou < iou_min: continue
                d = ((pc[0]-oc[0])**2 + (pc[1]-oc[1])**2)**0.5
                pairs.append((d, pi, ji))
        pairs.sort(key=lambda x:x[0])

        taken_p=set(); taken_o=set(); conf_map={}
        for _,pi,ji in pairs:
            if pi in taken_p or ji in taken_o: 
                continue
            taken_p.add(pi); taken_o.add(ji)
            conf_map[pi] = float(ppe_list[ji]["conf"])
        return conf_map, taken_o

    # Sıkı kuralla eşleştir
    h_map, taken_h = match(helmets, "helmet")
    v_map, taken_v = match(vests,   "vest")

    # Yelek için yedek kural (yatay merkez kişi içinde + gevşek IoU ≥ 0.03)
    remaining_v = [v for idx,v in enumerate(vests) if idx not in taken_v]
    if remaining_v:
        pairs=[]
        for pi,pb,pc,_,_,_ in people:
            if pi in v_map: 
                continue
            for ji,obj in enumerate(remaining_v):
                ob=obj["box"]; oc=center_of(ob)
                if not (pb[0] <= oc[0] <= pb[2]): continue
                iou2 = fast_iou(pb, ob)
                if iou2 < 0.03: continue
                y1,y2 = pb[1], pb[3]
                if not (y1 + int(0.15*(y2-y1)) <= oc[1] <= y1 + int(0.98*(y2-y1))): continue
                d = ((pc[0]-oc[0])**2 + (pc[1]-oc[1])**2)**0.5
                pairs.append((d, pi, ji))
        pairs.sort(key=lambda x:x[0])
        used_p=set(); used_o=set()
        for _,pi,ji in pairs:
            if pi in used_p or ji in used_o or pi in v_map:
                continue
            v_map[pi] = float(remaining_v[ji]["conf"])
            used_p.add(pi); used_o.add(ji)

    out=[]
    for i,p in enumerate(persons):
        hc = h_map.get(i, 0.0)
        vc = v_map.get(i, 0.0)
        safe = (hc >= min_h and vc >= min_v)
        out.append({"box": p["box"], "safe": safe, "h": hc, "v": vc})
    return out

def draw_boxes(img, status):
    for s in status:
        x1,y1,x2,y2 = s["box"]
        color = (0,200,0) if s["safe"] else (0,0,255)
        txt   = "Güvenli" if s["safe"] else "Güvensiz"
        cv2.rectangle(img,(x1,y1),(x2,y2),color,3)
        cv2.putText(img, txt, (x1,max(0,y1-8)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    return img

# ================== AKIŞ ==================
uploaded = st.file_uploader("📂 Video yükleyin", type=["mp4", "mov", "avi", "mkv"])

if uploaded:
    # temp dosya
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(uploaded.read()); tfile.flush()
    cap = cv2.VideoCapture(tfile.name)

    if not cap.isOpened():
        st.error("🚫 Video açılamadı.")
    else:
        src_fps = cap.get(cv2.CAP_PROP_FPS)
        try:
            if not src_fps or src_fps != src_fps or src_fps <= 0 or src_fps > 120:
                src_fps = 25.0
        except:
            src_fps = 25.0
        frame_delay = 1.0/src_fps

        st.success(f"✅ Video yüklendi — cihaz: {DEVICE}, FPS: {src_fps:.1f}")
        stframe = st.empty()  # TEK placeholder (ekrana resim yığmaz)

        # Kayıt (işlenmiş görüntü boyutunda)
        out_w, out_h = 1280, 720
        out_path = os.path.join(OUTPUT_DIR, f"processed_{int(time.time())}.mp4")
        writer = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"mp4v"),
                                 src_fps if KEEP_SOURCE_FPS else src_fps,
                                 (out_w, out_h))

        last_vote = None
        last_announce = 0.0

        while True:
            t0 = time.perf_counter()

            ret, frame = cap.read()
            if not ret: break

            img = enhance(frame)

            # ——— TESPİTLER (GPU/CPU otomatik) ———
            rh = human_model.predict(source=img, device=DEVICE, half=HALF,
                                     imgsz=IMG_SIZE, conf=HUMAN_TH, verbose=False)[0]
            persons = parse(rh, human_model.names, {"person"}, HUMAN_TH)

            rp = ppe_model.predict(source=img, device=DEVICE, half=HALF,
                                   imgsz=IMG_SIZE, conf=min(HELMET_TH, VEST_TH), verbose=False)[0]
            # Tek çağrıda hepsi; sonra filtrele
            all_objs = []
            for b in rp.boxes:
                conf=float(b.conf[0])
                lbl = norm_label(ppe_model.names[int(b.cls[0])])
                if lbl in {"helmet","vest"} and conf >= (HELMET_TH if lbl=="helmet" else VEST_TH):
                    x1,y1,x2,y2 = map(int, b.xyxy[0])
                    all_objs.append({"box":(x1,y1,x2,y2), "conf":conf, "label":lbl})
            helmets = [o for o in all_objs if o["label"]=="helmet"]
            vests   = [o for o in all_objs if o["label"]=="vest"]

            # ——— EŞLEŞTİR + ÇİZ ———
            debug_canvas = img if SHOW_DEBUG else None
            status = assign(persons, helmets, vests,
                            iou_min=IOU_MIN, min_h=MIN_H_CONF, min_v=MIN_V_CONF,
                            debug_img=debug_canvas, show_debug=SHOW_DEBUG)
            vis = draw_boxes(img.copy(), status)

            # Tek placeholder’a yaz (yığılma yok)
            stframe.image(cv2.cvtColor(vis, cv2.COLOR_BGR2RGB), channels="RGB")

            # Videoya yaz
            writer.write(vis)

            # Sadece durum değişince bilgi ver (banner yerine kısa)
            safe_cnt = sum(1 for s in status if s["safe"])
            total    = len(status)
            vote = (safe_cnt, total)
            if vote != last_vote and time.time()-last_announce > 1.0:
                st.toast(f"Güncel durum • Güvenli: {safe_cnt} / Toplam: {total}", icon="✅" if safe_cnt==total and total>0 else "⚠️")
                last_vote = vote
                last_announce = time.time()

            # ——— FPS’te oynatma: işleme süresini telafi ederek bekle ———
            elapsed = time.perf_counter() - t0
            to_wait = frame_delay - elapsed
            if to_wait > 0:
                time.sleep(to_wait)

        cap.release()
        writer.release()
        try: os.remove(tfile.name)
        except: pass

        st.success(f"🎬 İşlenmiş video kaydedildi: {out_path}")
        with open(out_path, "rb") as f:
            st.download_button("📥 Videoyu indir", f, file_name=os.path.basename(out_path), mime="video/mp4")
