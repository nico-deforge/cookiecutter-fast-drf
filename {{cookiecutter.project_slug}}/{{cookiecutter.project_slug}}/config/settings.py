"""
Django settings for {{cookiecutter.project_slug}} project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
from typing import List

import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "dev"),
)
# reading .env file
environ.Env.read_env(env_file=".env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ
DEBUG = env("DEBUG")

# dev if not in os.environ
ENVIRONMENT = env("ENVIRONMENT")

# django-cors-headers library authorization
if ENVIRONMENT == "dev":
    ALLOWED_HOSTS = ["*"]
    CORS_ORIGIN_ALLOW_ALL = True
else:
    ALLOWED_HOSTS = []
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST: List[str] = []

# Application definition
if ENVIRONMENT in ["preprod", "prod"]:
    INSTALLED_APPS = [
        "{{cookiecutter.project_slug}}.core.apps.CoreConfig",
        "rest_framework",
        "corsheaders",
        "drf_yasg",
        "django_filters",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django.contrib.postgres",
        "django_cleanup.apps.CleanupConfig",
        "import_export",
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
    ]
else:
    INSTALLED_APPS = [
        "{{cookiecutter.project_slug}}.core.apps.CoreConfig",
        "rest_framework",
        "corsheaders",
        "drf_yasg",
        "django_filters",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django.contrib.postgres",
        "debug_toolbar",
        "django_cleanup.apps.CleanupConfig",
        "import_export",
    ]

    MIDDLEWARE = [
        "corsheaders.middleware.CorsMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

ROOT_URLCONF = "{{cookiecutter.project_slug}}.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "{{cookiecutter.project_slug}}.config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}

AUTH_USER_MODEL = "core.User"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

if ENVIRONMENT in ["preprod", "prod"]:
    STATIC_ROOT = os.path.join(BASE_DIR, "public/static")

# Session settings
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True  # Avoid javascript hack
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # To keep the user logged in
SESSION_COOKIE_AGE = 1209600  # Two weeks cookie duration in seconds
if ENVIRONMENT in ["dev", "test"]:
    SESSION_COOKIE_SECURE = False  # True in production
else:
    SESSION_COOKIE_SECURE = True  # True in production

# Email sender settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
EMAIL_HOST = "smtp-relay.sendinblue.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

# Messages settings
MESSAGE_STORAGE = "django.contrib.messages.storage.fallback.FallbackStorage"

# Site class settings
SITE_ID = 1

# rest framework settings
if ENVIRONMENT == "dev":
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ),
        "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
        "DEFAULT_PERMISSION_CLASSES": (
            "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        ),
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "TEST_REQUEST_DEFAULT_FORMAT": "json",
        "PAGE_SIZE": 20,
        "EXCEPTION_HANDLER": "{{cookiecutter.project_slug}}.core.exceptions.exception_errors_format_handler",
    }
else:
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
        "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
        "DEFAULT_PERMISSION_CLASSES": (
            "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        ),
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "TEST_REQUEST_DEFAULT_FORMAT": "json",
        "PAGE_SIZE": 20,
        "DEFAULT_THROTTLE_CLASSES": [
            "rest_framework.throttling.AnonRateThrottle",
            "rest_framework.throttling.UserRateThrottle",
        ],
        "DEFAULT_THROTTLE_RATES": {"anon": "1000/day", "user": "10000/day"},
        "EXCEPTION_HANDLER": "{{cookiecutter.project_slug}}.core.exceptions.exception_errors_format_handler",
    }

# djoser auth library settings
DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "account/password/new/{uid}/{token}",
    "ACTIVATION_URL": "account/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": False,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "TOKEN_MODEL": None,
    "SERIALIZERS": {},
    "EMAIL": {
        "activation": "{{cookiecutter.project_slug}}.core.email.CustomActivationEmail",
        "password_reset": "{{cookiecutter.project_slug}}.core.email.CustomPasswordResetEmail",
    },
}

# simple jwt library settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": env("SECRET_KEY"),
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# Django-storages settings
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "app-" + ENVIRONMENT + "-bucket"
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None


# API documentation library settings
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Basic": {"type": "basic"},
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"},
    }
}

# Define IPS Adresses for Django debug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# django-import-export library settings
IMPORT_EXPORT_USE_TRANSACTIONS = True