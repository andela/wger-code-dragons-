#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dj_database_url
import psycopg2
from wger.settings_global import *


# Use 'DEBUG = True' to get more details for server errors
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True
STATIC_ROOT = os.path.join(SITE_ROOT, 'staticfiles')
ADMINS = (
    ('Your name', 'your_email@example.com'),
)
MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
        }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e_e^a#btn1a76r@y9@76pplm)kk8f&5zgtjkv22i-5*#_3^z0-'

# Your reCaptcha keys
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
NOCAPTCHA = True
SOCIAL_AUTH_FACEBOOK_KEY = '1269407003109297'
SOCIAL_AUTH_FACEBOOK_SECRET = '2658385dee664cda0f0b446b6aecd671'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '283272038266-5snsealg791ohlthh79toih4753ebsvj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'je2c-T13lEtmMOSpasqh1-M0'
SOCIAL_AUTH_TWITTER_KEY = 'RRXsckKpSk9Tpyyw8WElcUldQ'
SOCIAL_AUTH_TWITTER_SECRET = 'dgSq3ijeKn3DWFf1OHkO6XE7IbdcsPIXGZkWBr7bfv1MhTY9z2'
# The site's URL (e.g. http://www.my-local-gym.com or http://localhost:8000)
# This is needed for uploaded files and images (exercise images, etc.) to be
# properly served.
SITE_URL = 'http://localhost:8000'
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, '/static/'),
    os.path.join(SITE_ROOT, '/static/bower_components/bootstrap/dist/js/'),
    os.path.join(SITE_ROOT, '/static/bower_components/shariff/build/')
)
STATIC_ROOT = os.path.join(SITE_ROOT, 'staticfiles')
STATICFILES_DIRS = (os.path.join(SITE_ROOT, "core", "static"),
                    os.path.join(SITE_ROOT, "nutrition", "static"),
                    os.path.join(SITE_ROOT, "weight", "static"),
                    os.path.join(SITE_ROOT, "exercises", "static"),
                    os.path.join(SITE_ROOT, "software", "static"),
                    os.path.join(SITE_ROOT, "core/static", "bower_components")
)
#  Add the Whitenoise to your Django application 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFiles Storage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # added BowerFinder to list of static file finders
    'djangobower.finders.BowerFinder',

    # Django compressor
    'compressor.finders.CompressorFinder',
)
BOWER_COMPONENTS_ROOT = os.path.join(SITE_ROOT, "static", "bower_components")

# Path to uploaded files
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(SITE_ROOT, "core", "media")
#MEDIA_ROOT = '/Users/kjoenzau/.local/share/wger/media'
MEDIA_URL = '/media/'

# Allow all hosts to access the application. Change if used in production.
ALLOWED_HOSTS = '*'

# This might be a good idea if you setup memcached
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Configure a real backend in production
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sender address used for sent emails
WGER_SETTINGS['EMAIL_FROM'] = 'wger Workout Manager <wger@example.com>'

# Your twitter handle, if you have one for this instance.
#WGER_SETTINGS['TWITTER'] = ''
