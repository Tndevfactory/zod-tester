"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from decouple import config
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# print("checking basedir")
# print(BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-1dxjl5esiz-ri&h^e_2sl^y#79@a&7j9bk95+!o+^d$kio-62$'
SECRET_KEY = os.getenv('SECRET_KEY', config('SECRET_KEY')),

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# SECRET_KEY = config('SECRET_KEY')
DEBUG = os.getenv('DEBUG', config('DEBUG', default=True, cast=bool)),
# print("checking env var")
# print(DEBUG)
# print(config('SECRET_KEY'))
# print(config('MONGODB_URI'))
# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', config('ALLOWED_HOSTS')),
# print(ALLOWED_HOSTS)
# os.environ['HOME'] = 'os environ set to home'
# print(os.getenv('HOME', config('MONGODB_URI')))
# print(os.getenv('MONGODB_URI', config('MONGODB_URI')))
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cnam',
    'cnrps',
    'cnss',
    'steg',
    'telecom',
    'rest_framework',
    'auth'

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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'zod',
#         'HOST': 'localhost',
#         'PORT': '27017'
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('DB_NAME', config('DB_NAME')),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': os.getenv('MONGODB_URI', config('MONGODB_URI')),
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
