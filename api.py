from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import io
from ultralytics import YOLO

app = FastAPI()
model = YOLO("Ekipman_Tespit_Modeli/best.pt")  # Model yolun bu olmalı

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    image_np = np.array(image)

    results = model(image_np)[0]
    response = []

    for box in results.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        label = results.names[class_id]
        response.append({
            "label": label,
            "confidence": f"{confidence:.2f}"
        })

    return JSONResponse(content={"detections": response})
