import os
from pathlib import Path

import environ
import structlog

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

PROJECT_NAME = env.str("PROJECT_NAME", default="Sidewinder")

DEBUG = env.bool("DJANGO_DEBUG")

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django_extensions",
    "allauth",
    "allauth.account",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "bulma",
    "django_htmx",
    "appname.core",
]

if DEBUG:
    INSTALLED_APPS += [
        "silk",
        "django_browser_reload",
        "debug_toolbar",
    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "django_structlog.middlewares.RequestMiddleware",
]

if DEBUG:
    MIDDLEWARE += [
        "silk.middleware.SilkyMiddleware",
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]
    DJANGO_DEBUG_TOOLBAR = env.bool("DJANGO_DEBUG_TOOLBAR")
    if DJANGO_DEBUG_TOOLBAR:
        MIDDLEWARE += [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]
    # Set to True only when analyzing queries
    # as it can have unexpected behavior
    SILKY_ANALYZE_QUERIES = False

ROOT_URLCONF = "appname.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "appname.core.context_processors.global_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "appname.wsgi.application"

# Database

DATABASES = {"default": env.db_url('DJ_DATABASE_CONN_STRING', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')}
CONN_MAX_AGE = None
CONN_HEALTH_CHECKS = True

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []

# Email

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = env.str("DJANGO_DEFAULT_FROM_EMAIL")
SERVER_EMAIL = env.str("DJANGO_SERVER_EMAIL")
EMAIL_HOST = env.str("DJANGO_EMAIL_HOST")
EMAIL_PORT = env.str("DJANGO_EMAIL_PORT")
EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]

# Defaults

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "core.User"

# Static files

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", str(BASE_DIR.joinpath("staticfiles")))

# Media

MEDIA_URL = "media/"
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", str(BASE_DIR.joinpath("media")))

# HTTPS settings

if env.bool("DJANGO_SSL", True):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

# DJANGO-ALLAUTH

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_SUBJECT_PREFIX = env.str("ALLAUTH_ACCOUNT_EMAIL_SUBJECT_PREFIX")

ACCOUNT_FORMS = {
    "login": "allauth.account.forms.LoginForm",
    "signup": "appname.core.forms.AcceptTermsSignupForm",
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "disconnect": "allauth.socialaccount.forms.DisconnectForm",
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]

# Django REST Framework

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

# drf-spectacular

SPECTACULAR_SETTINGS = {
    "TITLE": PROJECT_NAME,
    "DESCRIPTION": "",
    "VERSION": "1.0.0",
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(),
        },
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.KeyValueRenderer(
                key_order=["timestamp", "level", "event", "logger"]
            ),
        },
        "rich": {"datefmt": "[%X]"},
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console",
        },
        "json_console": {
            "class": "logging.StreamHandler",
            "formatter": "json_formatter",
        },
    },
    "loggers": {
        "django_structlog": {
            "handlers": ["json_console"],
            "level": "INFO",
        },
        "django": {
            "handlers": ["json_console"],
            "level": "INFO",
        },
        "core": {
            "handlers": ["json_console"],
            "level": "INFO",
        },
    },
}

if DEBUG:
    LOGGING["handlers"]["flat_line_file"] = {
        "class": "logging.handlers.WatchedFileHandler",
        "filename": "logs/flat_line.log",
        "formatter": "key_value",
    }
    LOGGING["handlers"]["sql_line_file"] = {
        "class": "logging.handlers.WatchedFileHandler",
        "filename": "logs/flat_line.log",
        "filters": ["require_debug_true"],
    }
    LOGGING["handlers"]["rich_console"] = {
        "class": "rich.logging.RichHandler",
        "formatter": "rich",
    }
    LOGGING["loggers"]["django_structlog"]["handlers"] = ["flat_line_file"]
    LOGGING["loggers"]["django"] = {
        "handlers": ["rich_console", "flat_line_file"],
        "level": "INFO",
    }
    # LOGGING["loggers"]["django.db.backends"] = {
    #     "handlers": ["sql_line_file"],
    #     "level": "DEBUG"
    # }
    LOGGING["loggers"]["core"] = {
        "handlers": ["console", "flat_line_file"],
        "level": "DEBUG",
    }

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

# snoop

if DEBUG:
    import snoop

    snoop.install()
