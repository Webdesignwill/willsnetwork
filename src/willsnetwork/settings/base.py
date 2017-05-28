from __future__ import absolute_import

import os

import dj_database_url
from configurations import Configuration
from envparse import env

from willsnetwork.settings.mixins import WillsNetworkMixin


class Base(WillsNetworkMixin, Configuration):
    """
    Contains all the basic settings of the project.
    In different envs these settings can be overriden with mixins.
    Note that WillsNetwork is part of the Base.
    The only reason this is put in Mixins, is because it keeps those settings
    nicely seperate.

    Hence, if you want to add a new custom settings, it's prefered to do so
    in the lighthouse sparks mixin.

    WN_ --> a custom settings
    others --> in base
    to override willsnetwork or other settings, you can do so in the
    respective env settings.
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))))

    @property
    def SECRET_KEY(self):
        return env('SECRET_KEY')

    DEBUG = env('DEBUG', cast=bool, default=False)
    ALLOWED_HOSTS = []
    ADMINS = (
        ('Michael van de Waeter', 'info@ideallical.com'),
    )

    DEFAULT_FROM_EMAIL = 'noreply@example.com'

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        'rest_framework',
        'accounts',
        'willsnetwork',
        'rest_api',
        'contacts',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ROOT_URLCONF = 'willsnetwork.urls'
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            },
        },
    ]
    WSGI_APPLICATION = 'willsnetwork.wsgi.application'

    DATABASES = dict(default=dj_database_url.config())

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
        },
    ]

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'Europe/Amsterdam'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_URL = '/static/'

    @property
    def STATIC_ROOT(self):
        return os.path.join(self.BASE_DIR, 'static')

    STATICFILES_STORAGE = ('whitenoise.storage.'
                           'CompressedManifestStaticFilesStorage')

    STATIC_URL = '/static/'
    FAVICON_PATH = STATIC_URL + 'images/favicon.png'

    AUTH_USER_MODEL = 'accounts.User'
    LOGIN_URL = '/login/'
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL = '/'

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ),
        'PAGE_SIZE': 10,
    }
