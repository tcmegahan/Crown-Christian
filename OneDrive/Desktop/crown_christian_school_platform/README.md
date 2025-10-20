# Crown Christian School Platform

## Installed Modules

This platform includes the following Django apps:

- crm
- admissions
- sis
- finance
- communications
- calendarx
- admin_dashboard
- analytics
- mission
- scheduling
- academics
- library
- tutoring
- athletics
- clubs
- field_trips
- transport
- maintenance
- store
- lunch
- events
- fundraising
- daycare
- surveys
- board
- ptf
- adult_learning
- summer_camp
- integrations

## Usage

1. Add all apps to `INSTALLED_APPS` in `backend/core/settings.py`.
2. Set required settings (see installer instructions).
3. Install dependencies:

```sh
pip install django msal reportlab pillow requests
```

4. Run migrations:

```sh
python manage.py createsuperuser
```

6. Seed demo data:

```sh
python manage.py generate_chapel_poster
python manage.py generate_devotion_posters
```

8. Social automations:

```sh
python manage.py run_social_scheduler
python manage.py update_social_analytics
```

## Validation

To validate installation and demo data, run:

```sh
python manage.py validate_install
```

## Scheduling

- Schedule `run_social_scheduler` every 10 minutes
- Schedule `update_social_analytics` daily

---
For more details, see `apply_crown_full_bundle.py` and the installer output.

Create backups before major changes:

```bash
copy db.sqlite3 backups/db_backup_demo.sqlite3
```

## What’s Included

- Django project: **crown**
- Apps: common, students, staff, finance, admissions, financial_aid, ptf, discipline, curriculum, communications, events, chapel, devotions, donations, dashboards, api
- REST API (DRF) basics in `api`
- Demo seeder: `seed_demo` command + CSVs
- Simple Dashboard page with totals
- VS Code config + Docker files

## Notes

 Uses SQLite by default for simplicity. Switch to Postgres later if needed.
 Environment variables live in `.env` (copy `.env.example`).
 All code, data, and backups are isolated to this workspace for integrity.
