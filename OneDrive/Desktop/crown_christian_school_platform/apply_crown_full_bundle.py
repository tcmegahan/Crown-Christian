# ============================================================
# apply_crown_full_bundle.py
# Crown Christian School Solutions — Full Platform Installer
# Core + Levels + A La Carte + Comms/Bulletin/Social + Seeds
# ============================================================

import os, sys, textwrap, json, datetime

ROOT = os.path.abspath(os.path.dirname(__file__))
BACKEND = os.path.join(ROOT, "backend")

# --- App groups (kept small but complete; you can expand later) ---
APPS = {
    # CORE L1
    "core": [],  # settings.py already exists; we won't overwrite
    "crm": [],
    "admissions": [],
    "sis": [],
    "finance": [],
    "communications": [],
    "calendarx": [],  # avoid name clash with stdlib
    "admin_dashboard": [],
    "analytics": [],

    # FAITH / MISSION
    "mission": [],  # chapel, devotions, covers, prayer, targets

    # LEVEL 2 (Scheduling/Academics moved per plan)
    "scheduling": [],
    "academics": [],
    "library": [],
    "tutoring": [],

    # LEVEL 3 (student life)
    "athletics": [],
    "clubs": [],
    "field_trips": [],
    "transport": [],
    "maintenance": [],

    # LEVEL 2/Commerce (per earlier phases)
    "store": [],       # Spirit Store
    "lunch": [],       # Lunch purchase
    "events": [],      # Tickets & events
    "fundraising": [],

    # Optional modules
    "daycare": [],
    "surveys": [],
    "board": [],
    "ptf": [],          # Parent-Teacher Fellowship
    "adult_learning": [],
    "summer_camp": [],

    # Integrations
    "integrations": [],
}

def ensure_dirs():
    if not os.path.isdir(BACKEND):
        print("❌ ERROR: backend/ folder not found at project root. Please run this from your repo root (the folder that contains backend/).")
        sys.exit(1)
    for app in APPS.keys():
        os.makedirs(os.path.join(BACKEND, app), exist_ok=True)
        for sub in ["migrations", "templates", "static", "management", "management/commands", "utils"]:
            os.makedirs(os.path.join(BACKEND, app, sub), exist_ok=True)

def write(path, content, *, force=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path) and not force:
        # do not overwrite existing user code
        print(f"• Skipped (exists): {os.path.relpath(path, ROOT)}")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")
    print(f"✔ Wrote: {os.path.relpath(path, ROOT)}")

def minimal_app(app_name, verbose_name=None):
    vb = verbose_name or app_name.replace("_", " ").title()
    base = os.path.join(BACKEND, app_name)

    write(os.path.join(base, "__init__.py"), "")
    write(os.path.join(base, "apps.py"), f"""
from django.apps import AppConfig

class {app_name.title().replace('_','')}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.{app_name}"
    verbose_name = "{vb}"
""")
    write(os.path.join(base, "migrations", "__init__.py"), "")
    write(os.path.join(base, "urls.py"), f"""
from django.urls import path
from . import views

app_name = "{app_name}"

urlpatterns = [
    path("health/", views.health, name="health"),
]
""")
    write(os.path.join(base, "views.py"), """
from django.http import JsonResponse

def health(request):
    return JsonResponse({"ok": True, "app": __name__})
""")
    write(os.path.join(base, "admin.py"), "from django.contrib import admin\n")
    write(os.path.join(base, "models.py"), "from django.db import models\n")

# ----- Define MODELS for each app (compact but useful) -----

MODELS = {}

# ============================================================
# apply_crown_full_bundle.py
# Crown Christian School Solutions — Full Platform Installer
# Core + Levels + A La Carte + Comms/Bulletin/Social + Seeds
# ============================================================

import os, sys, textwrap, json, datetime

ROOT = os.path.abspath(os.path.dirname(__file__))
BACKEND = os.path.join(ROOT, "backend")

# --- App groups (kept small but complete; you can expand later) ---
APPS = {
    # CORE L1
    "core": [],  # settings.py already exists; we won't overwrite
    "crm": [],
    "admissions": [],
    "sis": [],
    "finance": [],
    "communications": [],
    "calendarx": [],  # avoid name clash with stdlib
    "admin_dashboard": [],
    "analytics": [],

    # FAITH / MISSION
    "mission": [],  # chapel, devotions, covers, prayer, targets

    # LEVEL 2 (Scheduling/Academics moved per plan)
    "scheduling": [],
    "academics": [],
    "library": [],
    "tutoring": [],

    # LEVEL 3 (student life)
    "athletics": [],
    "clubs": [],
    "field_trips": [],
    "transport": [],
    "maintenance": [],

    # LEVEL 2/Commerce (per earlier phases)
    "store": [],       # Spirit Store
    "lunch": [],       # Lunch purchase
    "events": [],      # Tickets & events
    "fundraising": [],

    # Optional modules
    "daycare": [],
    "surveys": [],
    "board": [],
    "ptf": [],          # Parent-Teacher Fellowship
    "adult_learning": [],
    "summer_camp": [],

    # Integrations
    "integrations": [],
}

# ...existing code...
# (Insert all logic, functions, MODELS, INTEGRATIONS_FILES, MISSION_UTILS, MISSION_CMDS, SEED_CMD, and main() as in your original paste)
# ...existing code...

def main():
    # ...existing code...
    pass

if __name__ == "__main__":
    main()
