"""
Django settings for timesheet project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ETC_DIR = '/etc/'

APP_NAME = 'timesheet'

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'timesheet.bhp.org.bw:8000'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9kygaeek(77$#ijdccizkj_)$dmd=21zl&3v95+4*42y3+stln'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

# KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_appointment.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_facility.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'bhp_personnel.apps.AppConfig',
    'timesheet_dashboard.apps.AppConfig',
    'timesheet.apps.EdcBaseAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'timesheet.urls'

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

WSGI_APPLICATION = 'timesheet.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'timesheet', 'static')

# dashboards
DASHBOARD_URL_NAMES = {
    'timesheet_listboard_url': 'timesheet_dashboard:timesheet_listboard_url',
    'timesheet_employee_listboard_url': 'timesheet_dashboard:timesheet_employee_listboard_url',
    'timesheet_calendar_table_url': 'timesheet_dashboard:timesheet_calendar_table_url',
    'reports_dashboard_url': 'timesheet_dashboard:reports_dashboard_url',
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'timesheet/base.html',
    'dashboard_base_template': 'timesheet/base.html',
    'timesheet_listboard_template': 'timesheet_dashboard/timesheet_listboard.html',
    'timesheet_employee_listboard_template': 'timesheet_dashboard/employee_listboard.html',
    'reports_dashboard_template': 'timesheet_dashboard/reports/dashboard.html',
}

