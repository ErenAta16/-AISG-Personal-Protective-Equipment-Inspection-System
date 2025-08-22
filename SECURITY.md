# Güvenlik Politikası

## 🛡️ Güvenlik Açığı Bildirimi

AISG KKD Denetim Sistemi'nde güvenlik açığı bulduysanız, lütfen aşağıdaki adımları takip edin:

### 📧 Güvenlik Açığı Bildirimi

**ÖNEMLİ**: Güvenlik açıklarını public GitHub issues'da bildirmeyin. Bunun yerine:

1. **E-posta ile bildirin**: xrlab@mcbu.edu.tr
2. **Konu satırında**: `[SECURITY] Güvenlik Açığı - [Kısa Açıklama]`
3. **Güvenlik açığının detaylarını** e-postada açıklayın

### 🔒 Güvenlik Açığı Bildirim Formatı

```
Konu: [SECURITY] Güvenlik Açığı - [Kısa Açıklama]

Güvenlik Açığı Detayları:
- Açıklama: [Detaylı açıklama]
- Etkilenen Sürüm: [Sürüm numarası]
- Etkilenen Bileşen: [Bileşen adı]
- CVE ID: [Varsa]

Tekrar Etme Adımları:
1. [Adım 1]
2. [Adım 2]
3. [Adım 3]

Beklenen Davranış:
[Ne olması gerekiyordu]

Gerçek Davranış:
[Ne oldu]

Ek Bilgiler:
[Ek detaylar, screenshot'lar, vb.]
```

## ⏰ Yanıt Süreleri

- **İlk yanıt**: 24 saat içinde
- **Güvenlik açığı değerlendirmesi**: 72 saat içinde
- **Düzeltme planı**: 1 hafta içinde
- **Düzeltme yayınlama**: Güvenlik açığına bağlı olarak 1-4 hafta

## 🔐 Güvenlik Önlemleri

### Veri Güvenliği
- Tüm veri iletişimi HTTPS üzerinden şifrelenir
- Hassas veriler şifrelenerek saklanır
- API anahtarları güvenli şekilde yönetilir

### Kimlik Doğrulama
- Güçlü şifre politikası
- Multi-factor authentication (MFA) desteği
- Session timeout yönetimi

### Erişim Kontrolü
- Role-based access control (RBAC)
- Principle of least privilege
- Audit logging

## 🚨 Güvenlik Uyarıları

### Kritik Güvenlik Açıkları
- Remote code execution
- SQL injection
- Cross-site scripting (XSS)
- Authentication bypass

### Orta Seviye Güvenlik Açıkları
- Information disclosure
- Cross-site request forgery (CSRF)
- Directory traversal
- Insecure deserialization

### Düşük Seviye Güvenlik Açıkları
- Security misconfiguration
- Outdated dependencies
- Weak encryption
- Missing security headers

## 🔄 Güvenlik Güncellemeleri

### Otomatik Güncellemeler
- Dependency vulnerability scanning
- Security patch deployment
- Automated security testing

### Manuel Güncellemeler
- Güvenlik açığı düzeltmeleri
- Security configuration updates
- Security policy changes

## 📋 Güvenlik Kontrol Listesi

### Geliştirme Süreci
- [ ] Security code review
- [ ] Vulnerability scanning
- [ ] Penetration testing
- [ ] Security testing automation

### Deployment Süreci
- [ ] Security configuration review
- [ ] Access control verification
- [ ] Security monitoring setup
- [ ] Incident response plan

### Maintenance Süreci
- [ ] Regular security updates
- [ ] Security audit logging
- [ ] Vulnerability assessment
- [ ] Security training

## 🆘 Acil Durum Planı

### Güvenlik İhlali Durumunda
1. **Hemen bildirin**: xrlab@mcbu.edu.tr
2. **Sistemi izole edin**: Gerekirse offline alın
3. **Veri yedeklerini koruyun**: Yedeklerin güvenliğini sağlayın
4. **Log'ları koruyun**: Tüm log dosyalarını saklayın
5. **İletişim kurun**: Etkilenen kullanıcıları bilgilendirin

### İletişim Kanalları
- **Güvenlik E-postası**: xrlab@mcbu.edu.tr
- **Acil Durum**: [Telefon numarası]
- **Teknik Destek**: [Teknik destek e-postası]

## 📚 Güvenlik Kaynakları

### Dokümantasyon
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python-security.readthedocs.io/)
- [Flask Security Documentation](https://flask-security.readthedocs.io/)

### Araçlar
- [Bandit](https://bandit.readthedocs.io/) - Python security linter
- [Safety](https://pyup.io/safety/) - Dependency vulnerability scanner
- [OWASP ZAP](https://owasp.org/www-project-zap/) - Web application scanner

## 🤝 Güvenlik Katkıları

Güvenlik iyileştirmeleri için katkıda bulunmak istiyorsanız:

1. **Güvenlik önerilerini** GitHub Discussions'da paylaşın
2. **Security-focused pull request** oluşturun
3. **Güvenlik dokümantasyonunu** güncelleyin
4. **Security testing** ekleyin

## 📞 İletişim

### Güvenlik Ekibi
- **Güvenlik Sorumlusu**: [İsim]
- **Teknik Güvenlik**: [İsim]
- **Güvenlik Danışmanı**: [İsim]

### Kurum Bilgileri
- **MCBU Manisa Teknik Bilimler MYO**
- **XRLab (Genişletilmiş Gerçeklik Laboratuvarı)**
- **E-posta**: xrlab@mcbu.edu.tr

---

**MCBÜ XRLab © 2025 - Tüm Hakları Saklıdır.**

**Son Güncelleme**: 2025-01-27
