# Crown2 API (Django)

This repository contains a Django application scaffold.

## Local development

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
. .venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create `.env` from `.env.example` and set appropriate values.

4. Run migrations and start development server:

```powershell
python manage.py migrate
python manage.py runserver
```

## Docker

Build the image:

```powershell
docker build -t crown2_api .
```

Run container:

```powershell
docker run -p8000:8000 --env-file .env crown2_api
```

## CI/CD

- CI checks run via `.github/workflows/python-ci.yml`.
- Azure deploy workflow: `.github/workflows/azure-deploy.yml` (requires GitHub secrets `AZURE_WEBAPP_NAME` and `AZURE_WEBAPP_PUBLISH_PROFILE`).

## Next steps

- Replace `SECRET_KEY` and set `DEBUG=False` for production.
- Configure a production database (Postgres recommended) and migrations.
- Configure monitoring and backups.
