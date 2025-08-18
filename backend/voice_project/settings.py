from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-%@a-r31p6jjh#h*w(ggi+phut=$xp2q&s$-j2of!j)enr^cl04'
)

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    ".onrender.com,127.0.0.1,localhost"
).split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "voice_auth",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",   # ✅ must be first
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "voice_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "voice_project.wsgi.application"

# ✅ Database
if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.config(default=os.environ["DATABASE_URL"], conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ✅ Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ CORS setup
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # vite dev
    "http://127.0.0.1:5173",
    "https://voice-finger-print-system.vercel.app",  # vercel frontend
]

# Allow all origins only in DEBUG (development)
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True

# ✅ CSRF trusted origins (must match your frontend + backend)
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
    "https://voice-finger-print-system.vercel.app",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ Custom user model
AUTH_USER_MODEL = "voice_auth.User"
