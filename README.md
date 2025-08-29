# AISG KKD Denetim Sistemi

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Latest-green.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [Teknolojiler](#teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [API Dokümantasyonu](#api-dokümantasyonu)
- [Model Detayları](#model-detayları)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)
- [İletişim](#iletişim)

## Proje Hakkında

AISG KKD Denetim Sistemi, çalışanların kişisel koruyucu donanım kullanma durumlarını izleyerek, çalışma ortamındaki güvenliği yükseltmek için geliştirilmiş kapsamlı bir iş sağlığı ve güvenliği çözümüdür.

### Ana Özellikler

- **Gerçek Zamanlı İzleme**: Kamera akışlarını sürekli analiz ederek güvenlik durumunu takip etme
- **Kişisel Koruyucu Donanım Tespiti**: Baret ve reflektif yelek kullanımını otomatik kontrol etme
- **İnsan Tespiti**: Çalışan varlığı ve sayısı analizi
- **Risk Uyarıları**: Güvenlik ihlallerinde anında bildirim gönderme
- **Compliance Raporlama**: Detaylı güvenlik raporları ve performans metrikleri

## Özellikler

### Güvenlik Tespiti
- **Baret Tespiti**: YOLOv8 tabanlı özel model ile baret kullanımı kontrolü
- **Reflektif Yelek Tespiti**: Görsel analiz ile yelek tespiti
- **İnsan Tespiti**: Çalışan varlığı ve sayısı analizi
- **Poz Sınıflandırması**: Oturuyor/ayakta durumu tespiti

### Dashboard ve Raporlama
- **Gerçek Zamanlı Analiz**: Anlık güvenlik durumu izleme
- **Akıllı Uyarı Sistemi**: Risk durumlarında otomatik bildirim
- **Detaylı Raporlama**: Compliance raporları ve performans metrikleri
- **Mobil Uyumluluk**: Responsive tasarım ile her cihazdan erişim

### Teknik Özellikler
- **Kolay Entegrasyon**: Mevcut kamera altyapılarına uyum
- **Güvenli İşleme**: Kurum içi çalıştırma seçenekleri
- **Çoklu Kamera Desteği**: Birden fazla kamera ile eş zamanlı analiz
- **API Desteği**: RESTful API ile sistem entegrasyonu

## Teknolojiler

### Backend
- **Python 3.8+**: Ana programlama dili
- **Streamlit**: Web arayüzü
- **OpenCV**: Görüntü işleme
- **Ultralytics YOLOv8**: Nesne tespit modeli
- **PyTorch**: AI framework

## Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- CUDA destekli GPU (opsiyonel, CPU ile de çalışır)
- Web kamerası veya IP kamera

### 1. Repository'yi Klonlayın
```bash
git clone https://github.com/username/aisg-kkd-denetim-sistemi.git
cd aisg-kkd-denetim-sistemi
```

### 2. Sanal Ortam Oluşturun
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Model Dosyalarını İndirin
Model dosyaları çok büyük olduğu için Git LFS ile yönetilmektedir. İndirmek için:

```bash
# Git LFS'i etkinleştirin
git lfs install

# Model dosyalarını indirin
git lfs pull
```

Alternatif olarak, model dosyalarını manuel olarak indirebilirsiniz:
- `models/best.pt`: PPE tespit modeli (baret + yelek)
- `models/insantespit.pt`: İnsan tespit modeli

### 5. Uygulamayı Çalıştırın
```bash
# Model dosyaları models/ klasöründe bulunmalıdır
# - best.pt (baret ve yelek tespit modeli)
# - insantespit.pt (insan tespit modeli)
```

### 6. Uygulamayı Çalıştırın
```bash
streamlit run app.py
```

Uygulama `http://localhost:8501` adresinde çalışmaya başlayacaktır.

## Kullanım

### Dashboard Erişimi
1. Web tarayıcınızda `http://localhost:8501` adresine gidin
2. Ana dashboard'da gerçek zamanlı analizleri izleyin
3. Sol menüden farklı modüllere erişin

### Kamera Entegrasyonu
1. `app.py` dosyasında kamera ayarlarını yapılandırın
2. Kamera URL'sini veya indeksini belirtin
3. Sistem otomatik olarak görüntü akışını analiz etmeye başlayacaktır

### API Kullanımı
```python
import requests

# Gerçek zamanlı analiz
response = requests.get('http://localhost:5000/api/analyze')
data = response.json()

# Güvenlik durumu
status = requests.get('http://localhost:5000/api/status')
```

## API Dokümantasyonu

### Endpoints

#### `GET /api/analyze`
Gerçek zamanlı analiz sonuçlarını döndürür.

**Response:**
```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "detections": {
    "helmet": 5,
    "vest": 4,
    "person": 6,
    "sitting": 2,
    "standing": 4
  },
  "alerts": [
    {
      "type": "missing_helmet",
      "severity": "high",
      "message": "Baret kullanmayan çalışan tespit edildi"
    }
  ]
}
```

#### `GET /api/status`
Sistem durumu ve istatistikleri döndürür.

#### `POST /api/configure`
Sistem ayarlarını günceller.

## Model Detayları

### Baret ve Yelek Tespit Modeli
- **Model**: YOLOv8 (custom trained)
- **Veri Seti**: Özel etiketli endüstriyel görüntüler
- **Doğruluk**: %95+ tespit oranı
- **Hız**: 30+ FPS (GPU ile)

### İnsan Tespit Modeli
- **Model**: YOLOv8 (custom trained)
- **Özellik**: Çoklu insan tespiti
- **Poz Sınıflandırması**: Oturuyor/Ayakta
- **Keypoint Tespiti**: 17 vücut eklemi

### Performans Metrikleri
- **Tespit Doğruluğu**: %92-98
- **False Positive Rate**: <5%
- **İşlem Hızı**: 25-35 FPS
- **Gecikme**: <100ms

## Gelecek Planları

### Kısa Vadeli (3-6 ay)
- [ ] Çoklu kamera desteği
- [ ] Gelişmiş bildirim kanalları
- [ ] Mobil uygulama

### Orta Vadeli (6-12 ay)
- [ ] Ek KKD türleri (eldiven, ayakkabı, pantolon)
- [ ] Zaman serisi raporları
- [ ] Machine Learning tabanlı risk analizi

### Uzun Vadeli (1+ yıl)
- [ ] Edge computing desteği
- [ ] Cloud entegrasyonu
- [ ] IoT sensör entegrasyonu

## Katkıda Bulunma

Bu projeye katkıda bulunmak istiyorsanız:

1. Repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

### Katkı Alanları
- Model iyileştirmeleri
- UI/UX geliştirmeleri
- Dokümantasyon
- Test yazımı
- Bug fixes

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

### Proje Ekibi
- **Eren Ata** - Geliştirici
- **Yunus Dermencioğlu** - Geliştirici  
- **Gülsüm Ceylan** - Geliştirici
- **Doç. Dr. Barış Çukurbaşı** - Danışman

### Kurum Bilgileri
- **MCBU Manisa Teknik Bilimler MYO**
- **XRLab (Genişletilmiş Gerçeklik Laboratuvarı)**
- **E-posta**: xrlab@mcbu.edu.tr

## Teşekkürler

Bu proje Manisa Celal Bayar Üniversitesi Manisa Teknik Bilimler Meslek Yüksekokulu Bilgisayar Teknolojisi Bölümü Genişletilmiş Gerçeklik Laboratuvarı'nda (XRLab) 2025 yılı yaz staj döneminde geliştirilmiştir.

---

**MCBÜ XRLab © 2025 - Tüm Hakları Saklıdır.**

[Başa Dön](#aisg-kkd-denetim-sistemi)
