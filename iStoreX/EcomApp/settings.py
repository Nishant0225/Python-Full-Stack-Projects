"""
Django settings for EcomApp project.
"""

from pathlib import Path
import os

# ======================
# BASE
# ======================
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================
# SECURITY (FORCE FIX)
# ======================
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-render-force-fallback"
)

DEBUG = True  # 🔥 MUST be True for now

# 🔥 ACCEPT ALL HOSTS (RENDER FIX)
ALLOWED_HOSTS = ["*"]

# ❌ REMOVE CSRF TRUST COMPLETELY
CSRF_TRUSTED_ORIGINS = []

# ======================
# APPLICATIONS
# ======================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
]

# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ======================
# URLS / TEMPLATES
# ======================
ROOT_URLCONF = "EcomApp.urls"

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
    },
]

WSGI_APPLICATION = "EcomApp.wsgi.application"

# ======================
# DATABASE
# ======================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ======================
# I18N
# ======================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ======================
# STATIC FILES (WHITENOISE)
# ======================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ======================
# MEDIA
# ======================
MEDIA_URL = "/uploads/"
MEDIA_ROOT = BASE_DIR / "uploads"

# ======================
# AUTH
# ======================
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/profile/"
LOGOUT_REDIRECT_URL = "/"

# ======================
# RENDER PROXY (SAFE)
# ======================
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = False

# ======================
# DEFAULT PK
# ======================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
