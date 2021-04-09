import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['*']
DEBUG = False

SECRET_KEY = os.environ.get(
    "SECRET_KEY", 'trp)7+j_n5^%a(%@itwn242@eq0d#m=ybtdl7_6j!%cg(is6e$')

HOME_PAGE_MESSAGE = "Hello World. This Is Production."
print("Using production")

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
    }
}
