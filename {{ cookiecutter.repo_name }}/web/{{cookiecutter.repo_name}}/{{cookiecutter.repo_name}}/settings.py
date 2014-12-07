import os
from configurations import Configuration, values
from unipath import Path


class Base(Configuration):
    LANGUAGE_CODE = '{{cookiecutter.language}}'

    TIME_ZONE = '{{cookiecutter.time_zone}}'

    ADMINS = (
        ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
    )
    MANAGERS = ADMINS

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    ALLOWED_HOSTS = [
    ]

    PROJECT_DIR = Path(__file__).ancestor(2)

    STATIC_ROOT = '/static/'
    STATICFILES_DIRS = (
        PROJECT_DIR.child('{{cookiecutter.repo_name}}', 'static'),
    )
    STATIC_URL = '/static/'

    MEDIA_ROOT = '/media/'
    MEDIA_URL = '/media/'

    TEMPLATE_DIRS = (
        PROJECT_DIR.child('templates'),
    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'django.core.context_processors.csrf',

        'stepup.context_processors.debug',
    )

    DATABASES = values.DatabaseURLValue()

    EMAIL = values.EmailURLValue()

    SECRET_KEY = values.Value()

    SITE_ID = 1

    ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

    WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',

        'django.contrib.admindocs',

        '{{cookiecutter.repo_name}}',
    ]

    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.admindocs.middleware.XViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': os.environ['DJANGO_HIREDIS_CACHE_LOCATION'],
            'OPTIONS': {
                'DB': 1,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
            }
        },
    }


class Dev(Base):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    INTERNAL_IPS = (
        '127.0.0.1',
    )

    MIDDLEWARE_CLASSES = Base.MIDDLEWARE_CLASSES + [
        # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        # 'debug_toolbar',
    ]


class Prod(Base):
    ALLOWED_HOSTS = Base.ALLOWED_HOSTS + [
        os.environ['DJANGO_ALLOWED_HOSTS'],
    ]

    RAVEN_CONFIG = values.DictValue()

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'raven.contrib.django.raven_compat',
    ]
