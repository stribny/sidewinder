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
    "django.forms",
    "django_extensions",
    "allauth",
    "allauth.account",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "drf_standardized_errors",
    "corsheaders",
    "django_htmx",
    "huey.contrib.djhuey",
    "bx_django_utils",
    "huey_monitor",
    "appname.core",
]

if DEBUG:
    INSTALLED_APPS += [
        "silk",
        "django_browser_reload",
        "debug_toolbar",
    ]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
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

DATABASES = {
    "default": env.db_url(
        "DJ_DATABASE_CONN_STRING", default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
    )
}
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
SMTP_DEV = env.bool("SMTP_DEV", 0)
ADMIN_EMAIL = env.str("ADMIN_EMAIL")

if DEBUG and SMTP_DEV:
    EMAIL_USE_TLS = False

if DEBUG and not SMTP_DEV:
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

FORM_RENDERER = "appname.core.forms.CustomFormRenderer"

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
    "DEFAULT_SCHEMA_CLASS": "drf_standardized_errors.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}
# Enable for seeing standard errors for unhandled exceptions if DEBUG=True
# DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}


# drf-spectacular

SPECTACULAR_SETTINGS = {
    "TITLE": PROJECT_NAME,
    "DESCRIPTION": "",
    "VERSION": "1.0.0",
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": "drf_standardized_errors.openapi_serializers.ValidationErrorEnum.values",
        "ClientErrorEnum": "drf_standardized_errors.openapi_serializers.ClientErrorEnum.values",
        "ServerErrorEnum": "drf_standardized_errors.openapi_serializers.ServerErrorEnum.values",
        "ErrorCode401Enum": "drf_standardized_errors.openapi_serializers.ErrorCode401Enum.values",
        "ErrorCode403Enum": "drf_standardized_errors.openapi_serializers.ErrorCode403Enum.values",
        "ErrorCode404Enum": "drf_standardized_errors.openapi_serializers.ErrorCode404Enum.values",
        "ErrorCode405Enum": "drf_standardized_errors.openapi_serializers.ErrorCode405Enum.values",
        "ErrorCode406Enum": "drf_standardized_errors.openapi_serializers.ErrorCode406Enum.values",
        "ErrorCode415Enum": "drf_standardized_errors.openapi_serializers.ErrorCode415Enum.values",
        "ErrorCode429Enum": "drf_standardized_errors.openapi_serializers.ErrorCode429Enum.values",
        "ErrorCode500Enum": "drf_standardized_errors.openapi_serializers.ErrorCode500Enum.values",
    },
    "POSTPROCESSING_HOOKS": [
        "drf_standardized_errors.openapi_hooks.postprocess_schema_enums"
    ],
}

# CORS

CORS_ALLOW_ALL_ORIGINS = True
CORS_URLS_REGEX = r"^/api/.*$"

# HUEY

HUEY = {
    "huey_class": "huey.PriorityRedisExpireHuey",
    "url": env.str("REDIS_URL", default="redis://127.0.0.1:6379?db=1"),
}

# Set to True to bypass redis in development
HUEY_DEV = env.bool("HUEY_DEV", default=True)
if not HUEY_DEV and DEBUG:
    HUEY["immediate_use_memory"] = False
    HUEY["immediate"] = False

# Shell plus from django-extensions

SHELL_PLUS = "ipython"
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_IMPORTS = [
    "from appname.core.services.email import EmailService",
]

# Logging


def clean_dev_console_processor(logger, method_name, event_dict):
    """
    Custom structlog processor to remove unnecessary information
    for development console to make the output cleaner.
    """

    event_dict.pop("request_id", None)
    event_dict.pop("ip", None)
    event_dict.pop("user_id", None)
    event_dict.pop("user_agent", None)
    return event_dict


timestamper = structlog.processors.TimeStamper(fmt="iso")

shared_structlog_processors = [
    structlog.contextvars.merge_contextvars,
    structlog.stdlib.add_log_level,
    structlog.stdlib.add_logger_name,
    timestamper,
]
conditional_processors = (
    [clean_dev_console_processor] if DEBUG else [structlog.processors.format_exc_info]
)
shared_structlog_processors += conditional_processors

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
    ]
    + shared_structlog_processors
    + [
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processors": [
                structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                structlog.processors.JSONRenderer(),
            ],
            "foreign_pre_chain": shared_structlog_processors,
        },
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processors": [
                structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                structlog.dev.ConsoleRenderer(),
            ],
            "foreign_pre_chain": shared_structlog_processors,
        },
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processors": [
                structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                structlog.processors.KeyValueRenderer(
                    key_order=["timestamp", "level", "event", "logger"]
                ),
            ],
            "foreign_pre_chain": shared_structlog_processors,
        },
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
            "formatter": "json",
        },
        "json_file": {
            "class": "logging.handlers.WatchedFileHandler",
            "formatter": "json",
            "filename": "logs/json.log",
        },
        "flat_file": {
            "class": "logging.handlers.WatchedFileHandler",
            "formatter": "key_value",
            "filename": "logs/flat_file.log",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["json_console"],
            "level": "INFO",
        },
        "django_structlog": {
            "level": "INFO",
        },
        "django": {
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["json_console"],
            "level": "INFO",
            "propagate": False,
        },
        "huey": {
            "level": "INFO",
        },
        "appname": {
            "level": "INFO",
        },
    },
}

if DEBUG:
    LOGGING["loggers"]["root"] = {
        "handlers": ["console", "json_file", "flat_file"],
    }
    LOGGING["loggers"]["django_structlog"] = {
        "level": "CRITICAL",
    }
    LOGGING["loggers"]["django.server"] = {
        "handlers": ["console"],
        "level": "INFO",
    }
    LOGGING["loggers"]["appname"] = {
        "level": "DEBUG",
    }
    # Uncomment to log SQL statements to console
    # LOGGING["loggers"]["django.db.backends"] = {
    #     "handlers": ["console"],
    #     "level": "DEBUG",
    #     "propagate": False,
    # }

# snoop

if DEBUG:
    import snoop

    snoop.install()

    from rich.traceback import install as install_rich_traceback

    install_rich_traceback(show_locals=True)
