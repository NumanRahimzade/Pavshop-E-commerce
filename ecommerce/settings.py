"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
import datetime
from django.utils.translation import gettext_lazy as _



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d0ifd+%e)(rj^3067@q1%@^3_5zjxni+ofg-3v)@fu=2fkpu!u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True




ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'account.User'
# Application definition

INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    # 'jet.dashboard',
    # 'jet',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',
    'rest_framework',
    'rest_framework_simplejwt',

    'core',
    'blog.apps.BlogConfig',
    'order',
    'account',
    'product.apps.ProductConfig',
    'django_countries',     #country ucun
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ecommerce.middleware.BlockIPMiddleware',
    # 'ecommerce.middleware.RequestLogMiddleware',
]


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=30),
    "TOKEN_OBTAIN_SERIALIZER": "account.api.serializers.CustomTokenObtainPairSerializer",
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,

    'JTI_CLAIM': 'jti',
}


ROOT_URLCONF = 'ecommerce.urls'

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
                'core.context_processor.subject_renderer',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
)


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '720891829993-2lfueg4vkjbgarmatrpji0bvll8polsm.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_FACEBOOK_KEY = '667685387860037'      
SOCIAL_AUTH_FACEBOOK_SECRET = '750bbce4e040d3c0cdfae4b482653b51'


WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tech',
        'USER': 'user',
        'PASSWORD': '12345',
        'PORT': 5432,
        'HOST': 'localhost',
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
}

LOGS_ROOT = BASE_DIR / f'logs/{datetime.date.today()}.log'


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

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'


SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = (

    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'account.pipeline.get_avatar', # This is the path of your pipeline.py
    #and get_avatar is the function.
)



# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('az', _('Azerbaijan')),

]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('en', _('English')),
    ('az', _('Azerbaijan')),
    
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%m/%d/%Y",
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# JET_THEMES = [
#     {
#         'theme': 'default', # theme folder name
#         'color': '#47bac1', # color of the theme's button in user menu
#         'title': 'Default' # theme title
#     },
#     {
#         'theme': 'green',
#         'color': '#44b78b',
#         'title': 'Green'
#     },
#     {
#         'theme': 'light-green',
#         'color': '#2faa60',
#         'title': 'Light Green'
#     },
#     {
#         'theme': 'light-violet',
#         'color': '#a464c4',
#         'title': 'Light Violet'
#     },
#     {
#         'theme': 'light-blue',
#         'color': '#5EADDE',
#         'title': 'Light Blue'
#     },
#     {
#         'theme': 'light-gray',
#         'color': '#222',
#         'title': 'Light Gray'
#     }
# ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'numanrahimzade@gmail.com'
EMAIL_HOST_PASSWORD = 'tptaxxlqwsawkcns'


