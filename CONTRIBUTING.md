# Katkıda Bulunma Rehberi

AISG KKD Denetim Sistemi projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Bu rehber, projeye nasıl katkıda bulunabileceğinizi açıklamaktadır.

## 🚀 Başlangıç

### Gereksinimler
- Python 3.8+
- Git
- GitHub hesabı

### Kurulum
1. Repository'yi fork edin
2. Lokal kopyayı klonlayın:
   ```bash
   git clone https://github.com/YOUR_USERNAME/aisg-kkd-denetim-sistemi.git
   cd aisg-kkd-denetim-sistemi
   ```
3. Remote origin'i ekleyin:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/aisg-kkd-denetim-sistemi.git
   ```
4. Upstream'i ekleyin:
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/aisg-kkd-denetim-sistemi.git
   ```

## 🔧 Geliştirme Süreci

### 1. Issue Oluşturma
- Yeni özellik veya bug fix için issue oluşturun
- Issue'da detaylı açıklama yapın
- Etiketleri (labels) uygun şekilde kullanın

### 2. Branch Oluşturma
```bash
git checkout -b feature/your-feature-name
# veya
git checkout -b fix/your-bug-fix
```

### 3. Geliştirme
- Kod standartlarına uyun
- Test yazın
- Dokümantasyonu güncelleyin

### 4. Commit
```bash
git add .
git commit -m "feat: add new feature description"
```

### 5. Push ve Pull Request
```bash
git push origin feature/your-feature-name
```

## 📝 Kod Standartları

### Python
- PEP 8 standartlarına uyun
- Type hints kullanın
- Docstring yazın
- Maksimum satır uzunluğu: 127 karakter

### Commit Mesajları
Conventional Commits standardını kullanın:
- `feat:` Yeni özellik
- `fix:` Bug düzeltmesi
- `docs:` Dokümantasyon değişiklikleri
- `style:` Kod formatı değişiklikleri
- `refactor:` Kod refactoring
- `test:` Test ekleme veya düzenleme
- `chore:` Build süreci veya yardımcı araçlar

### Örnek Commit Mesajları
```
feat: add helmet detection model
fix: resolve camera stream issue
docs: update API documentation
style: format code according to PEP 8
```

## 🧪 Test Yazımı

### Test Gereksinimleri
- Her yeni özellik için test yazın
- Test coverage'ı %80'in üzerinde tutun
- Unit testler ve integration testler yazın

### Test Çalıştırma
```bash
# Tüm testleri çalıştır
pytest

# Coverage ile test çalıştır
pytest --cov=./ --cov-report=html

# Belirli test dosyasını çalıştır
pytest tests/test_detection.py
```

## 📚 Dokümantasyon

### Güncellenmesi Gereken Dosyalar
- README.md
- API dokümantasyonu
- Kod içi docstring'ler
- Kurulum rehberi

### Dokümantasyon Standartları
- Markdown formatı kullanın
- Kod örnekleri ekleyin
- Screenshot'lar ekleyin
- Türkçe ve İngilizce destekleyin

## 🔍 Code Review Süreci

### Pull Request Oluşturma
1. Açıklayıcı başlık yazın
2. Değişiklikleri detaylı açıklayın
3. Screenshot'lar ekleyin (UI değişiklikleri için)
4. Test sonuçlarını ekleyin

### Review Kriterleri
- Kod kalitesi
- Test coverage
- Dokümantasyon güncellemeleri
- Performans etkisi
- Güvenlik değerlendirmesi

## 🐛 Bug Report

### Bug Report Formatı
```markdown
**Bug Açıklaması:**
Kısa ve net açıklama

**Tekrar Etme Adımları:**
1. Adım 1
2. Adım 2
3. Adım 3

**Beklenen Davranış:**
Ne olması gerekiyordu

**Gerçek Davranış:**
Ne oldu

**Sistem Bilgileri:**
- OS: [Windows/Mac/Linux]
- Python Version: [3.8/3.9/3.10/3.11]
- Browser: [Chrome/Firefox/Safari]

**Ek Bilgiler:**
Screenshot'lar, log'lar, vb.
```

## 💡 Özellik Önerisi

### Özellik Önerisi Formatı
```markdown
**Özellik Açıklaması:**
Ne eklenmesini istiyorsunuz?

**Kullanım Senaryosu:**
Bu özellik nasıl kullanılacak?

**Alternatif Çözümler:**
Varsa alternatif yaklaşımlar

**Ek Bilgiler:**
Screenshot'lar, mockup'lar, vb.
```

## 🏷️ Etiketler (Labels)

### Issue Etiketleri
- `enhancement`: Yeni özellik
- `bug`: Bug report
- `documentation`: Dokümantasyon
- `help wanted`: Yardım gerekli
- `good first issue`: Yeni başlayanlar için
- `priority: high`: Yüksek öncelik
- `priority: medium`: Orta öncelik
- `priority: low`: Düşük öncelik

## 📞 İletişim

### Sorularınız İçin
- GitHub Issues kullanın
- E-posta: xrlab@mcbu.edu.tr
- Proje ekibi ile iletişime geçin

### Topluluk
- Proje tartışmaları için GitHub Discussions kullanın
- Sorularınızı GitHub Issues'da sorun
- Diğer katkıda bulunanlarla işbirliği yapın

## 🙏 Teşekkürler

Projeye katkıda bulunduğunuz için teşekkür ederiz! Her katkı, AISG KKD Denetim Sistemi'ni daha iyi hale getirmemize yardımcı oluyor.

---

**MCBÜ XRLab © 2025 - Tüm Hakları Saklıdır.**
