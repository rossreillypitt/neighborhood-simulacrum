"""
Django settings for profiles project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from .local_settings import LOCAL_SECRET_KEY, DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASSWORD, LOCAL_DEBUG, \
    DATASTORE_HOST, DATASTORE_NAME, DATASTORE_PASSWORD, DATASTORE_PORT, DATASTORE_USER

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LOCAL_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = LOCAL_DEBUG

ALLOWED_HOSTS = ['api.profiles.wprdc.org', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'polymorphic',
    'corsheaders',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_extensions',
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'nested_admin',

    # local apps
    'indicators',
    'geo',
    'census_data',
    'maps',
    'public_housing',
    #  'debug_toolbar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'profiles.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'profiles.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    },
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': DATASTORE_HOST,
        'PORT': DATASTORE_PORT,
        'NAME': DATASTORE_NAME,
        'USER': DATASTORE_USER,
        'PASSWORD': DATASTORE_PASSWORD,
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    'long_term': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'long_term_cache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', ],

    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
}

CORS_ORIGIN_ALLOW_ALL = True

GRAPPELLI_ADMIN_TITLE = 'Profiles II'

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

INTERNAL_IPS = '127.0.0.1'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Profiles customization settings
# ```````````````````````````````
AVAILABLE_COUNTIES_IDS = ('42073', '42003', '42007', '42125', '42059',
                          '42051', '42129', '42063', '42005', '42019',)

MAP_HOST = 'https://api.profiles.wprdc.org/map_layer'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

AVAILABLE_GEOG_TYPES = (
    'blockGroup',
    'tract',
    'countySubdivision',
    # 'schoolDistrict',
    'county',
    'neighborhood',
    'zcta',
)

# todo: make it so these values are the defaults and any entries in settings replace them
SQ_ALIAS = 'dt'
GEO_ALIAS = '"GEO"'

GEOG_DKEY = '__geog__'
TIME_DKEY = '__time__'
VALUE_DKEY = '__value__'
DENOM_DKEY = '__denom__'

CKAN_API_BASE_URL = 'https://data.wprdc.org/api/3/'
DATASTORE_SEARCH_SQL_ENDPOINT = 'action/datastore_search_sql'

VIEW_CACHE_TTL = 0  # 60 * 60 # 60 mins

LONG_TERM_CACHE_TTL = 0  # 60 * 60 * 24  # 24 hours

USE_LONG_TERM_CACHE = False

