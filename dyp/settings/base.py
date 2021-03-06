"""
Django settings for dyp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#print BASE_DIR



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gp$sr*ty6knrplu&v5-o-vpzl1*5vj-de(_q!%#3d!j3*#s%54'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'favicon',
    'south',
    'joins',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dyp.middleware.ReferMiddleware'
)

ROOT_URLCONF = 'dyp.urls'

WSGI_APPLICATION = 'dyp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#SOUTH_DATABASE_ADAPTERS = {'default':'south.db.postgresql_psycopg2'}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#SHARE_URL = "http://dropyourprojects.com/?ref="

SHARE_URL = "http://127.0.0.1:8000/?ref="

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates')
) 
#'/Users/bharu_sathya/desktop/lwc/src/templates/',

 


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT = '/Users/bharu_sathya/desktop/lwc/src/static/static_root/'

STATIC_ROOT = os.path.join(BASE_DIR,'static','static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static','static_dirs'),


)

MEDIA_ROOT =os.path.join(BASE_DIR,'static','media')


MEDIA_URL = '/media/'

#FAVICON_PATH = os.path.join(TEMPLATE_DIRS,'favicon.ico')
