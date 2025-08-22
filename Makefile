# AISG KKD Denetim Sistemi Makefile
# Proje yönetimi için kullanışlı komutlar

.PHONY: help install test run clean docker-build docker-run docker-stop lint format

# Default target
help:
	@echo "AISG KKD Denetim Sistemi - Kullanılabilir Komutlar:"
	@echo ""
	@echo "  install      - Python bağımlılıklarını yükle"
	@echo "  test         - Testleri çalıştır"
	@echo "  run          - Uygulamayı çalıştır"
	@echo "  clean        - Geçici dosyaları temizle"
	@echo "  lint         - Kod kalitesi kontrolü"
	@echo "  format       - Kodu formatla"
	@echo "  docker-build - Docker image oluştur"
	@echo "  docker-run   - Docker container çalıştır"
	@echo "  docker-stop  - Docker container durdur"
	@echo "  setup        - Geliştirme ortamını kur"
	@echo "  deploy       - Production'a deploy et"

# Python environment setup
install:
	@echo "Python bağımlılıkları yükleniyor..."
	pip install -r requirements.txt
	@echo "Bağımlılıklar yüklendi!"

# Development environment setup
setup:
	@echo "Geliştirme ortamı kuruluyor..."
	python -m venv venv
	@echo "Sanal ortam oluşturuldu. Aktifleştirmek için:"
	@echo "Windows: venv\\Scripts\\activate"
	@echo "Linux/Mac: source venv/bin/activate"
	@echo "Sonra: make install"

# Run tests
test:
	@echo "Testler çalıştırılıyor..."
	pytest tests/ -v --cov=./ --cov-report=html
	@echo "Testler tamamlandı!"

# Run the application
run:
	@echo "AISG KKD Denetim Sistemi başlatılıyor..."
	python app.py

# Clean temporary files
clean:
	@echo "Geçici dosyalar temizleniyor..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	@echo "Temizlik tamamlandı!"

# Code linting
lint:
	@echo "Kod kalitesi kontrol ediliyor..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	@echo "Linting tamamlandı!"

# Code formatting
format:
	@echo "Kod formatlanıyor..."
	black .
	isort .
	@echo "Formatlama tamamlandı!"

# Docker commands
docker-build:
	@echo "Docker image oluşturuluyor..."
	docker build -t aisg-kkd-denetim:latest .

docker-run:
	@echo "Docker container çalıştırılıyor..."
	docker run -d -p 5000:5000 --name aisg-container aisg-kkd-denetim:latest

docker-stop:
	@echo "Docker container durduruluyor..."
	docker stop aisg-container
	docker rm aisg-container

# Docker Compose commands
docker-compose-up:
	@echo "Docker Compose ile servisler başlatılıyor..."
	docker-compose up -d

docker-compose-down:
	@echo "Docker Compose servisleri durduruluyor..."
	docker-compose down

docker-compose-logs:
	@echo "Docker Compose logları gösteriliyor..."
	docker-compose logs -f

# Production deployment
deploy:
	@echo "Production'a deploy ediliyor..."
	@echo "Bu komut production ortamına deploy işlemi yapar"
	@echo "Lütfen production ayarlarını kontrol edin"

# Development server with auto-reload
dev:
	@echo "Geliştirme sunucusu başlatılıyor..."
	export FLASK_ENV=development
	export FLASK_DEBUG=1
	python app.py

# Install development dependencies
install-dev:
	@echo "Geliştirme bağımlılıkları yükleniyor..."
	pip install -r requirements.txt
	pip install pytest pytest-cov flake8 black isort
	@echo "Geliştirme bağımlılıkları yüklendi!"

# Security check
security-check:
	@echo "Güvenlik kontrolü yapılıyor..."
	safety check
	bandit -r .
	@echo "Güvenlik kontrolü tamamlandı!"

# Performance test
perf-test:
	@echo "Performans testi yapılıyor..."
	python -m pytest tests/test_performance.py -v
	@echo "Performans testi tamamlandı!"

# Database operations
db-migrate:
	@echo "Veritabanı migration yapılıyor..."
	@echo "Migration komutları buraya eklenecek"

db-seed:
	@echo "Veritabanı seed data yükleniyor..."
	@echo "Seed data komutları buraya eklenecek"

# Backup
backup:
	@echo "Veri yedekleniyor..."
	@echo "Backup komutları buraya eklenecek"

# Restore
restore:
	@echo "Veri geri yükleniyor..."
	@echo "Restore komutları buraya eklenecek"

# Show system info
info:
	@echo "Sistem bilgileri:"
	@echo "Python version: $(shell python --version)"
	@echo "Pip version: $(shell pip --version)"
	@echo "Current directory: $(shell pwd)"
	@echo "Git status: $(shell git status --porcelain | wc -l) değişiklik"

# Update dependencies
update-deps:
	@echo "Bağımlılıklar güncelleniyor..."
	pip install --upgrade -r requirements.txt
	@echo "Bağımlılıklar güncellendi!"

# Show help for specific target
help-%:
	@echo "Hedef '$*' için yardım:"
	@grep -A 1 "^$*:" Makefile
