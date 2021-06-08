from datetime import timedelta

from .base import *  # noqa F403
from . import secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# django-cors-headers library authorization
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = []

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
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": secret.DB_NAME,
        "USER": secret.DB_USER_TEST,
        "PASSWORD": secret.DB_PASSWORD_TESTT,
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# djoser auth library settings
DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "account/password/new/{uid}/{token}",
    "ACTIVATION_URL": "account/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
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
    "SIGNING_KEY": secret.SECRET_KEY,
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

STATIC_ROOT = secret.STATIC_ROOT

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = secret.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = secret.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = "app-dev-bucket"
AWS_S3_REGION_NAME = secret.AWS_S3_REGION_NAME
AWS_S3_ENDPOINT_URL = secret.AWS_S3_ENDPOINT_URL
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

# Session settings
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True  # Avoid javascript hack
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # To keep the user logged in
SESSION_COOKIE_AGE = 1209600  # Two weeks cookie duration in seconds
SESSION_COOKIE_SECURE = True  # True in production
