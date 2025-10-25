# Makefile for local development tasks

PYTHON=python3

.PHONY: setup up migrate seed test build

setup:
	$(PYTHON) -m venv .venv
	.venv/bin/pip install -U pip
	.venv/bin/pip install -r apps/api/requirements-dev.txt
	cd apps/web && pnpm i || true

up:
	docker compose up --build

migrate:
	.venv/bin/python apps/api/manage.py makemigrations
	.venv/bin/python apps/api/manage.py migrate

seed:
	.venv/bin/python scripts/seed_sample_data.py

test:
	.venv/bin/pytest apps/api

build:
	docker build -f apps/api/Dockerfile -t crown360:local .
