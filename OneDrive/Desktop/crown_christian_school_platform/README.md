# Crown Christian School Platform (Clean Starter Bundle)

This is a clean, consolidated starter bundle aligned with your modules so you can restart in VS Code without the old errors.

## Quick Start (Local)

1. **Create & activate a virtualenv**
   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Django**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py seed_demo
   python manage.py runserver
   ```

4. Open http://127.0.0.1:8000 and /admin

## Docker (optional)
```bash
docker compose up --build
```

## What’s Included
- Django project: **crown**
- Apps: common, students, staff, finance, admissions, financial_aid, ptf, discipline, curriculum, communications, events, chapel, devotions, donations, dashboards, api
- REST API (DRF) basics in `api`
- Demo seeder: `seed_demo` command + CSVs
- Simple Dashboard page with totals
- VS Code config + Docker files

## Notes
- Uses SQLite by default for simplicity. Switch to Postgres later if needed.
- Environment variables live in `.env` (copy `.env.example`).
