import os

# all base settings for Django
from .base import *

from .installed import *

HOME_PAGE_MESSAGE = "Hello World. This Is A Local Proxy."
print("Using local proxy")

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production',
        'USER': 'dbproduser',
        'PASSWORD': 'elephant',
        'HOST': '127.0.0.1',
        'PORT': 6543,
    }
}
