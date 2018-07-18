# Django settings for testsite project.
import os
DIRNAME = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Testing Testerson', 'test@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django-ssl-redirect.db',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(DIRNAME, 'media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(DIRNAME, 'files/')
STATIC_URL = '/files/'

STATICFILES_DIRS = (
    os.path.join(DIRNAME, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'dkr+86m#8)$5b*y(c3n)jp5-kwr&amp;y+4a@tvi@rt2^h0e3%mnp^'

MIDDLEWARE = [
    'ssl_redirect.middleware.SSLRedirectMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'testsite.urls'

WSGI_APPLICATION = 'testsite.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(DIRNAME, 'templates/')],
        'APP_DIRS': False,
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

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testapp',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
