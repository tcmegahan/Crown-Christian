from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret')
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'rest_framework',
 'corsheaders',
 'drf_spectacular',
 'core',
 'academics',
 'finance',
 'comms',
]

MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'corsheaders.middleware.CorsMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
 {
 'BACKEND': 'django.template.backends.django.DjangoTemplates',
 'DIRS': [],
 'APP_DIRS': True,
 'OPTIONS': {
 'context_processors': [
 'django.template.context_processors.debug',
 'django.template.context_processors.request',
 'django.contrib.auth.context_processors.auth',
 'django.contrib.messages.context_processors.messages',
 ],
 },
 },
]

WSGI_APPLICATION = 'api.wsgi.application'

DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': BASE_DIR / 'db.sqlite3',
 }
}

STATIC_URL = '/static/'

REST_FRAMEWORK = {
 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
 'DEFAULT_PERMISSION_CLASSES': [
 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
 ],
}

SPECTACULAR_SETTINGS = {
 'TITLE': 'Crown2 API',
 'DESCRIPTION': 'API for Crown2',
 'VERSION': '0.1.0',
}

CORS_ALLOW_ALL_ORIGINS = True
