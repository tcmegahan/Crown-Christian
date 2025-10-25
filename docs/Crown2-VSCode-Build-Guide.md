# Crown² — VS Code Build Guide (Core + Startup Level)

Purpose: Hands-on instructions for engineers to stand up the Crown² Core + Startup tier in Visual Studio Code, using Microsoft365 for Education and Azure as the backbone. This guide covers environment setup, repository structure, dev containers, secrets, backend (Django/DRF), frontend (React/MUI), Teams app, Microsoft Graph, database models, APIs, CI/CD, and local test workflows.

##1) Prerequisites (workstation & cloud)

- VS Code latest + extensions: Python, Pylance, Ruff, Black, YAML, Docker, Dev Containers, Azure Tools, Azure CLI Tools, GitHub Copilot (optional), ESLint, Prettier, Teams Toolkit, Thunder Client or REST Client.
- Install toolchains: Python3.12, Node.js20 LTS, pnpm9.x, Docker Desktop, Azure CLI (az), Microsoft365 CLI (m365), Git2.40+, Make.
- Cloud: Azure subscription + M365 tenant with Education SKUs (A1/A3/A5). Create a Resource Group: `rg-crown2-dev`.
- Accounts: Service principal for CI/CD; App registrations for Web API (backend) and SPA (frontend/Teams).
- Power BI (Pro) for admin/report users (at least3) for Analytics Lite.

##2) Monorepo Layout

Suggested structure:

- `crown2/`
 - `infra/` # IaC templates (bicep/terraform) + GitHub Actions workflows
 - `apps/`
 - `api/` # Django/DRF backend (Azure App Service)
 - `web/` # React/MUI admin + parent/teacher SPA (Vite)
 - `teams/` # Teams app (tabs for Teacher & Parent) via Teams Toolkit
 - `packages/`
 - `ui/` # Shared UI components (TypeScript + MUI)
 - `sdk/` # Crown2 TypeScript/Python SDKs for API
 - `.devcontainer/` # Dev container config
 - `scripts/` # Helper scripts (seed, migrate, export)
 - `.github/workflows/` # CI/CD pipelines
 - `README.md` `LICENSE` `CODE_OF_CONDUCT.md`

##3) Dev Container

Use VS Code Dev Containers for reproducible builds. Example `.devcontainer/devcontainer.json`:

```json
{
 "name": "crown2-dev",
 "image": "mcr.microsoft.com/devcontainers/python:3.12",
 "features": { "ghcr.io/devcontainers/features/node:1": { "version": "20" } },
 "postCreateCommand": "pip install -U pip && pip install -r apps/api/requirements-dev.txt && pnpm i --prefix apps/web",
 "customizations": { "vscode": { "extensions": ["ms-python.python","ms-azuretools.vscode-azureappservice","azuredevcollege.azuretoolsforvscode","ms-vscode.vscode-node-azure-pack","ms-vscode.vscode-typescript-next","ms-Teams-vscode-extension.vscode-teams-toolkit"] } }
}
```

Adjust `postCreateCommand` to match your repo layout and dependency files.

##4) Secrets & Environment

- Use Azure Key Vault: `kv-crown2-dev`. Store DB connection string, Graph client secret, payment webhook secrets.
- Local dev: `apps/api/.env` and `apps/web/.env.local`. DO NOT commit. Example keys:
 - BACKEND: `DATABASE_URL=postgresql+psycopg://crown2:pw@localhost:5432/crown2`, `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `GRAPH_SCOPES`, `JWT_SECRET`, `STORAGE_ACCOUNT`, `SENDGRID_KEY` (or SMTP).
 - FRONTEND: `VITE_AUTH_CLIENT_ID`, `VITE_TENANT_ID`, `VITE_API_BASE_URL`, `VITE_TEAMS_APP_ID`, `VITE_POWERBI_WORKSPACE_ID`.

##5) Backend API (Django + DRF)

1. Create project: `cd apps && django-admin startproject api .` (or use existing scaffold).
2. Install deps: `pip install django djangorestframework drf-spectacular django-environ msal requests azure-identity azure-storage-blob azure-keyvault-secrets psycopg[binary] django-cors-headers`.
3. Enable apps in `settings.py`: `rest_framework`, `corsheaders`, `drf_spectacular`.
4. Auth: Use MSAL for OAuth2/OpenID with Azure AD. Map Azure AD `objectId` to User table; store minimal profile.
5. CORS & CSRF: allow SPA origin(s).
6. OpenAPI: drf-spectacular for `/schema` and Swagger UI.
7. Run: `python manage.py migrate && python manage.py createsuperuser`.

###5a) Initial Models (Core Data Model)

Create apps: `core`, `academics`, `finance`, `comms`. Key models:

- `Family`(household_id UUID, name, address, phone)
- `Guardian`(guardian_id UUID, family FK, first_name, last_name, email, phone)
- `Student`(student_id UUID, family FK, first_name, last_name, dob, grade_level, status)
- `Term`(term_id UUID, name, start_date, end_date)
- `Course`(course_id UUID, code, name, credits)
- `Section`(section_id UUID, course FK, term FK, teacher FK, period, room)
- `Enrollment`(enrollment_id UUID, student FK, section FK, status)
- `Attendance`(attendance_id UUID, student FK, section FK, date, code, note)
- `Grade`(grade_id UUID, student FK, section FK, term FK, score, scale, comment)
- `Ledger`(ledger_id UUID, family FK, opened_on)
- `LedgerLine`(line_id UUID, ledger FK, kind[INVOICE|PAYMENT|ADJUST], amount, memo, posted_on, external_ref)
- `Communication`(comm_id UUID, audience, channel[EMAIL|SMS|TEAMS], template, sent_on, meta JSON)

Run migrations after models are defined: `python manage.py makemigrations && python manage.py migrate`.

###5b) API Endpoints (DRF ViewSets)

- CRUD: families, guardians, students, terms, courses, sections, enrollments.
- Attendance: `POST /attendance/bulk` (list of (student, section, date, code)).
- Grades: `POST /grades/bulk`, `GET /report-cards?term_id=...`.
- Finance: `GET /ledger/{family_id}`, `POST /invoices`, `POST /payments/webhook`.
- Comms: `POST /messages/send` (audience query + template).
- Auth: `/auth/login` (AAD redirect), `/auth/me`, `/auth/logout`.

##6) Microsoft Graph & Teams Integration

- Register two apps in Entra ID: `crown2-api` (confidential) and `crown2-spa` (public).
- API exposes scopes; SPA requests MSAL tokens (PKCE).
- Use Microsoft Graph SDKs (Python for backend, TS for SPA).
- Roster sync: Use School Data Sync (SDS) post-acceptance to create classes/teams.
- Teams tabs: Use Teams Toolkit in `apps/teams` to scaffold Teacher and Parent tabs; configure SSO with Entra.

##7) Frontend Admin/Parent SPA (React + Vite + MUI)

- Scaffold: `pnpm create vite apps/web --template react-ts`; `pnpm i @mui/material @mui/icons-material @tanstack/react-query react-router-dom msal-browser msal-react axios zod`.
- App shell: top nav with role-based menu (Registrar, Business, Teacher, Parent).
- Pages: Dashboard, Students, Sections, Attendance, Grades, Billing (invoices, payments), Reports.
- Auth: MSAL React for AAD login; `acquireTokenSilent` for API calls; Axios interceptor adds bearer token.
- Table components with server-side pagination; form validation via zod/react-hook-form.
- Theme: light/dark; large touch targets for mobile.

##8) Parent Portal (SharePoint Communication Site + Teams App)

- Create a SharePoint Communication site named 'Crown2 Parent Portal'. Embed web SPA as a web part (if using SPFx) or provide deep links into the SPA. Add secure document libraries for handbooks, invoices, and forms. Package the same React app as a Teams tab for mobile access by parents.

##9) Payments & Accounting

- Integrate payment gateway (Stripe/Compuwerx). Webhook endpoint in Django receives payment confirmations, updates `Ledger` and creates `LedgerLine(PAYMENT)`. Nightly QuickBooks export job (CSV/IIF) posts summarized entries per day. Reconciliation report ensures export totals match ledger activity.

##10) Analytics Lite (Power BI)

- Create a Power BI workspace. Publish Attendance Trend, Invoice Aging, Enrollment Count reports. Embed reports in the admin SPA via Power BI JavaScript SDK; secure via AAD and role-based filters.

##11) CI/CD (GitHub Actions)

- Workflows: `api-ci.yml` (lint, test, build Docker, push to ACR), `web-ci.yml` (lint, test, build), `deploy.yml` (blue/green to Azure App Service).
- Secrets from Key Vault via OIDC federation; no long-lived secrets in GitHub.
- Run database migrations on deploy; apply static assets; warm-up health checks.

##12) Quality Gates

- Python: Ruff + Black + Pytest + coverage>85%.
- JS/TS: ESLint + Prettier + Vitest + Playwright E2E for core journeys (login, attendance entry, invoice pay).
- Conventional Commits; semantic-release (optional).
- Pre-commit hooks for lint/test on changed files.

##13) Local Dev (Docker Compose)

- Create `docker-compose.yml` with services: postgres, redis (future), api, web, and a mailhog container for dev email. Bind mounts to sync code; expose ports5173 (web) and8000 (api). Seed data script creates demo families/students.

##14) Make Targets

- `make setup` # create venv, install deps
- `make up` # docker compose up
- `make migrate`
- `make seed`
- `make test`
- `make deploy-dev`

##15) Milestones (12-week MVP)

Follow the sprint plan: S1–S12 with acceptance criteria. Gate releases by passing quality checks and user acceptance from Registrar and Business Office leads.

##16) Out of Scope for Core (defer to Growth)

- Full Financial Aid logic (Stewardship Paths) beyond tuition starter.
- Clubs/Athletics scheduling depth (eligibility engines).
- Donor/Advancement CRM, Alumni directory.
- Multi-language UI (beyond basic notices).
- Predictive analytics suite (beyond Analytics Lite).

---

Next steps (suggested):

1. Create the `.devcontainer` and `apps` monorepo scaffolding.
2. Scaffold `apps/api` Django project and add a minimal `requirements.txt`.
3. Add `docker-compose.yml` and `Makefile` for local developer workflows.

If you want, I can create any of the above now. Specify which item to start with and I will proceed.
