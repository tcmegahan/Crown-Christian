FROM python:3.10.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc libpq-dev build-essential curl \
 && python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get purge -y --auto-remove gcc build-essential \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*

COPY . ./

# Collect static files (do not fail build if settings not configured)
RUN mkdir -p /app/staticfiles \
 && python manage.py collectstatic --noinput || true

# Create non-root user (do not fail if not available in minimal images)
RUN addgroup --system appgroup || true \
 && adduser --system --ingroup appgroup --no-create-home appuser || true
USER appuser

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
 CMD curl -f http://localhost:8000/ || exit 1

CMD ["gunicorn", "crown2_api.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
