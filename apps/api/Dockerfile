FROM node:20-alpine AS node_build
WORKDIR /app/web
# Enable corepack for pnpm
RUN corepack enable && corepack prepare pnpm@9.0.0 --activate
# Copy frontend sources
COPY apps/web/package.json apps/web/pnpm-lock.yaml* ./
COPY apps/web/ ./
# Install and build
RUN pnpm install --frozen-lockfile && pnpm run build

#2) Python runtime
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
# System deps for Postgres and builds
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential libpq-dev gcc curl \
 && rm -rf /var/lib/apt/lists/*

# Copy only requirements and install (better caching)
COPY apps/api/requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY apps/api/ ./
