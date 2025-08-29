# AISG KKD Denetim Sistemi

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Latest-green.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Proje Hakkında

AISG KKD Denetim Sistemi, çalışanların kişisel koruyucu donanım kullanma durumlarını izleyerek, çalışma ortamındaki güvenliği yükseltmek için geliştirilmiş kapsamlı bir iş sağlığı ve güvenliği çözümüdür.

### Ana Özellikler

- **Gerçek Zamanlı İzleme**: Kamera akışlarını sürekli analiz ederek güvenlik durumunu takip etme
- **Kişisel Koruyucu Donanım Tespiti**: Baret ve reflektif yelek kullanımını otomatik kontrol etme
- **İnsan Tespiti**: Çalışan varlığı ve sayısı analizi
- **Risk Uyarıları**: Güvenlik ihlallerinde anında bildirim gönderme

## Teknolojiler

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
git clone <repository-url>
cd <repository-name>
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

### 4. Uygulamayı Çalıştırın
```bash
streamlit run app.py
```

## Kullanım

1. Uygulamayı başlattıktan sonra tarayıcınızda `http://localhost:8501` adresine gidin
2. Sol panelden tespit eşiklerini ayarlayın
3. Kamera veya video dosyası seçin
4. Gerçek zamanlı PPE tespitini izleyin

## Model Dosyaları

`models/` klasöründe aşağıdaki dosyalar bulunmalıdır:
- `best.pt`: PPE tespit modeli (baret + yelek)
- `insantespit.pt`: İnsan tespit modeli

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
