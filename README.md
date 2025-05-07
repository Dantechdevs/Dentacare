# Dentacare Clinic Management System

[![Django Version](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)

A comprehensive dental clinic management system with multi-role support and integrated modules.

## 📂 Project Structure
```bash
dentacare/
├── clinic/                  # Main Django application
│   ├── models/             # Database models
│   │   ├── employees.py     # HR management models
│   │   ├── patients.py      # Patient records
│   │   └── inventory.py     # Drug inventory system
│   │
│   ├── views/              # Business logic
│   ├── templates/           # Frontend components
│   └── tests/               # Unit tests
│
├── clinic_app/             # Core Django project
│   ├── settings/           # Configuration
│   ├── urls.py             # Routing
│   └── wsgi.py             # Deployment
│
├── requirements.txt        # Dependencies
└── manage.py               # Django CLI
```

## 🌟 Key Features
### Role-Based Access Control
- **Medical Staff**  
  - Patient treatment history tracking
  - Dental charting visualization
  - Appointment scheduling
- **HR Management**  
  - Employee onboarding workflows
  - Leave management system
  - Performance evaluation templates
- **Administration**  
  - Drug inventory alerts (low stock/expiry)
  - Payroll integration with tax calculations
  - Audit trails for record changes

### 📦 Modules
| Module | Technology Stack | Key Functionality |
|--------|------------------|-------------------|
| Patient Records | Django ORM + PostgreSQL | Medical history, X-ray storage, Allergy alerts |
| Payroll System | Python Decimal + Cronjobs | Automatic deductions, Payslip generation |
| Drug Inventory | Django REST Framework | Batch tracking, Supplier management, Expiry alerts |
| Appointment System | Celery + Redis | SMS reminders, Calendar sync, Conflict detection |

## 🛠️ Installation
1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables (create `.env`):
```ini
SECRET_KEY=your_django_secret
DEBUG=True
DB_NAME=dentacare_db
DB_USER=postgres_user
DB_PASSWORD=secure_password
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

## 🔧 Configuration
Update `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'clinic.apps.ClinicConfig',
    'rest_framework',
    'crispy_forms',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'clinic/static')]
```

## 📚 Documentation
- [API Docs](docs/api/README.md) - Endpoint specifications
- [User Manual](docs/user_guide.pdf) - Role-specific workflows
- [Database Schema](docs/db_schema.png) - ER diagram

## 🧪 Testing
Run test suite:
```bash
pytest --cov=clinic tests/
```

## 🚀 Deployment
### Docker Setup
```dockerfile
# Dockerfile
FROM python:3.10
RUN pip install gunicorn
COPY . /app
WORKDIR /app
```

```yaml
# docker-compose.yml
services:
  web:
    build: .
    command: gunicorn clinic_app.wsgi:application --bind 0.0.0.0:8000
    ports:
      - "8000:8000"
```

## 🤝 Contributing
1. Fork the repository
2. Create feature branch:
```bash
git checkout -b feature/new-module
```
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License
[MIT License](LICENSE)

## 🙏 Acknowledgments
- Django Software Foundation
- PostgreSQL Global Development Group
- Medical Data Working Group standards
