import os
from pathlib import Path

# Buduje ścieżki wewnątrz projektu tak jak: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- GŁÓWNA KONFIGURACJA ---
SECRET_KEY = "django-insecure-8ovil3xu6=eaoqd--#&ricv159p0pypoh5_lgm*)-dfcjqe=yc"
DEBUG = True
ALLOWED_HOSTS = []

# --- APLIKACJE ---
INSTALLED_APPS = [
    # Aplikacje Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Twoje aplikacje
    "taxi",
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- URLS / WSGI ---
ROOT_URLCONF = "taxi_service.urls"
WSGI_APPLICATION = "taxi_service.wsgi.application"

# 🛠️ KLUCZOWA ZMIANA: Konfiguracja szablonów
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Używamy os.path.join, aby zapewnić kompatybilność z Windows i wyeliminować błędy Pathlib.
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

# --- BAZA DANYCH ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- UŻYTKOWNICY ---
AUTH_USER_MODEL = "taxi.Driver"

# --- JĘZYK / CZAS ---
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- PLIKI STATYCZNE (CSS, JS, Obrazki) ---
STATIC_URL = "/static/"
# Django będzie szukać plików statycznych w folderze 'taxi/static/' (dzięki APP_DIRS)

# --- INNE ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"