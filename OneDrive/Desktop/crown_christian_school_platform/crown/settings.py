from pathlib import Path
import environ, os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, "django-insecure-change-me"),
    ALLOWED_HOSTS=(list, ["127.0.0.1", "localhost"]),
    TIME_ZONE=(str, "America/New_York"),
)
environ.Env.read_env(BASE_DIR / ".env")

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
TIME_ZONE = env("TIME_ZONE")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # backend apps only (no duplicates, only present apps)
    'backend.core','backend.crm','backend.admissions','backend.sis','backend.finance','backend.communications',
    'backend.calendarx','backend.admin_dashboard','backend.analytics','backend.mission','backend.scheduling','backend.academics','backend.library','backend.tutoring','backend.athletics','backend.clubs','backend.field_trips','backend.transport','backend.maintenance','backend.store','backend.lunch','backend.events','backend.fundraising','backend.daycare','backend.surveys','backend.board','backend.ptf','backend.adult_learning','backend.summer_camp','backend.integrations','backend.schedulemaster','backend.chapel','backend.activities','backend.adultlearning','backend.financial_aid','backend.donations','backend.discipline','students','dashboards'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "crown.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "crown.wsgi.application"

DATABASES = {
    "default": env.db(),
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True


STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Crown Full Bundle recommended settings ---
TIME_ZONE = "America/New_York"
USE_TZ = True

# Microsoft Graph
MS_GRAPH_TENANT_ID = os.getenv("MS_GRAPH_TENANT_ID", "YOUR_TENANT_ID")
MS_GRAPH_CLIENT_ID = os.getenv("MS_GRAPH_CLIENT_ID", "YOUR_CLIENT_ID")
MS_GRAPH_CLIENT_SECRET = os.getenv("MS_GRAPH_CLIENT_SECRET", "YOUR_CLIENT_SECRET")

# Branding & Assets
SCHOOL_LOGO_PATH = BASE_DIR / "static" / "images" / "crown_logo.png"
BULLETIN_QR_URL = "https://www.crownchristianschools.com/devotions"
DEFAULT_CHAPEL_BANNER = BASE_DIR / "static" / "images" / "chapel_default.jpg"
DEFAULT_DEVOTION_BANNER = BASE_DIR / "static" / "images" / "devotion_default.jpg"

# Social (use environment variables in production)
SOCIAL_FACEBOOK_PAGE_ID = os.getenv("SOCIAL_FACEBOOK_PAGE_ID", "")
SOCIAL_FACEBOOK_PAGE_ACCESS_TOKEN = os.getenv("SOCIAL_FACEBOOK_PAGE_ACCESS_TOKEN", "")
SOCIAL_INSTAGRAM_BUSINESS_ID = os.getenv("SOCIAL_INSTAGRAM_BUSINESS_ID", "")
SOCIAL_INSTAGRAM_ACCESS_TOKEN = os.getenv("SOCIAL_INSTAGRAM_ACCESS_TOKEN", "")
SOCIAL_DEFAULT_HASHTAGS = "#CrownChristian #Faith #Chapel #Devotion #ChristianEducation"




