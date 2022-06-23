from .debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store',
        'USER': 'store_user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}
