"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from environs import Env
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-jr6m%@3uvvqd(2)2^r!1)%qy8e)#_0*kuh1%#ydngt_ve0dmpr'
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# ALLOWED_HOSTS = []

# --- gstam ---
env = Env()
# In a production setting change .env.private with .env after initializing all fields in the .env file.
env.read_env(".env.private", recurse=False)
SECRET_KEY = env('SECRET_KEY')
DEVELOPMENT = env('DEVELOPMENT')

if DEVELOPMENT:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    CSRF_TRUSTED_ORIGINS = ['http://192.168.2.132:8000']
else:
    DEBUG = False
    # SECURITY WARNING: don't run with debug turned on in production!
    ALLOWED_HOSTS = ['utilities.dide.ira.net']
    # CSRF_COOKIE_SECURE = False
    CSRF_TRUSTED_ORIGINS = ['http://utilities.dide.ira.net']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': env('MYSQL_DATABASE'), 
            'USER': env('MYSQL_USER'),
            'PASSWORD': env('MYSQL_PASSWORD'),
            'HOST': env('MYSQL_HOST_IP'),
            'PORT': env('MYSQL_PORT'),
        }
 }
# *** gstam *** END


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Third Party
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'markdownx',
    # Local
    'accounts.apps.AccountsConfig',
    "webscripts.apps.WebscriptsConfig",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# django-crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# --- gstam ---
LOGIN_REDIRECT_URL = "home"
# LOGOUT_REDIRECT_URL = "home" # Set at the end of the file as  ACCOUNT_LOGOUT_REDIRECT = "home"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'el-GR' #'el-GR''en-US' 
LOCALE = 'el_gr@euro'
# DATE_INPUT_FORMATS = ['%d/%m/%Y','%d-%m-%Y']
TIME_ZONE = 'Europe/Athens'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
STATIC_ROOT = BASE_DIR / 'static/'
# --- gstam --- 


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.CustomUser'

# config/settings.py

# django-allauth config
SITE_ID = 1

ACCOUNT_LOGOUT_REDIRECT = "home"
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend", # new
)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL=env('DEFAULT_FROM_EMAIL')
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_USE_TLS=env('EMAIL_USE_TLS')
#EMAIL_USE_SSL="True"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}