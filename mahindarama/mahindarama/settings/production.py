import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['mahindarama-jv5lt5t3va-uw.a.run.app']
DEBUG = False

SECRET_KEY = os.environ.get(
    "SECRET_KEY", 'trp)7+j_n5^%a(%@itwn242@eq0d#m=ybtdl7_6j!%cg(is6e$')


print("Using production")

# Database

HOME_PAGE_MESSAGE = f"Hello World. This Is Production."

DB_USER_UN = os.environ.get("DB_USER_UN", '')
DB_USER_PW = os.environ.get("DB_USER_PW", 'abc')
DB_NAME = os.environ.get("DB_NAME", "production")
INSTANCE_CONNECTION_NAME = os.environ.get("INSTANCE_CONNECTION_NAME")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER_UN,
        'PASSWORD': DB_USER_PW,
        'HOST': f'/cloudsql/{INSTANCE_CONNECTION_NAME}',
    }
}
