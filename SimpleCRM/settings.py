"""
Django settings for SimpleCRM project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


#standard library
import logging
import os

#Django imports
from django.contrib.messages import constants as messages

#local imports
from logger import logger
try:
    import local
except:
    logger.warning('You need add local.py file with local settings ... ')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = local.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1',)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'crispy_forms',
    'widget_tweaks', # tool for templates
    'mycrm',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SimpleCRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates', './mycrm/templates'],
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

WSGI_APPLICATION = 'SimpleCRM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'OPTIONS': {
#            'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf')
#        },
#    }
#}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
]

# Beautiful messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

#after login
LOGIN_REDIRECT_URL = '/mycrm'

#Email config for reseting password
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = local.EMAIL
EMAIL_HOST_PASSWORD = local.EMAIL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#Only console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#TODO change static root
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'mycrm', 'static'),
]

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates'),
#     os.path.join(BASE_DIR, 'mycrm', 'templates'),
# )

#for debug purposes
logger.info(STATIC_URL)
logger.info('static root {}'.format(STATIC_ROOT))
logger.info('static file dirs {}'.format(STATICFILES_DIRS))
logger.info('there are following templates -> \n{}'.format(TEMPLATES))
# logger.info('Template dirs are here: {}'.format(TEMPLATE_DIRS))

CRISPY_TEMPLATE_PACK = 'bootstrap4' #Crispy theme

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
