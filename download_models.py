#!/usr/bin/env python3
"""
AISG KKD Denetim Sistemi - Model İndirme Scripti
Bu script, gerekli YOLO model dosyalarını indirir.
"""

import os
import requests
from pathlib import Path
import sys

def download_file(url, filename, chunk_size=8192):
    """Dosyayı chunk'lar halinde indirir."""
    print(f"İndiriliyor: {filename}")
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                
                # Progress bar
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(f"\rİlerleme: {percent:.1f}% ({downloaded}/{total_size} bytes)", end='')
    
    print(f"\n✅ {filename} başarıyla indirildi!")

def main():
    """Ana fonksiyon."""
    print("🚀 AISG KKD Denetim Sistemi - Model İndirme")
    print("=" * 50)
    
    # Models klasörünü oluştur
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    # Model URL'leri (örnek - gerçek URL'lerle değiştirilmeli)
    models = {
        "best.pt": "https://example.com/models/best.pt",  # PPE modeli
        "insantespit.pt": "https://example.com/models/insantespit.pt"  # İnsan tespit modeli
    }
    
    print("⚠️  ÖNEMLİ: Bu script örnek URL'ler kullanır.")
    print("Gerçek model dosyalarını indirmek için:")
    print("1. Model dosyalarını manuel olarak indirin")
    print("2. models/ klasörüne yerleştirin")
    print("3. Dosya isimlerinin doğru olduğundan emin olun")
    print()
    
    # Kullanıcıdan onay al
    response = input("Devam etmek istiyor musunuz? (y/N): ")
    if response.lower() != 'y':
        print("İptal edildi.")
        return
    
    # Model dosyalarını indir
    for filename, url in models.items():
        filepath = models_dir / filename
        
        if filepath.exists():
            print(f"⚠️  {filename} zaten mevcut, atlanıyor...")
            continue
            
        try:
            download_file(url, filepath)
        except Exception as e:
            print(f"❌ {filename} indirilemedi: {e}")
            print("Manuel indirme gerekli.")
    
    print("\n🎯 Model indirme tamamlandı!")
    print("📁 models/ klasörünü kontrol edin.")
    print("\n💡 Eğer model dosyaları indirilemediyse:")
    print("1. Manuel olarak indirin")
    print("2. models/ klasörüne yerleştirin")
    print("3. Dosya isimlerini kontrol edin")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ İptal edildi.")
    except Exception as e:
        print(f"\n❌ Hata: {e}")
        sys.exit(1)
