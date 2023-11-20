from quotesapp.base_settings import *

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS+=[

]

MIDDLEWARE+=[

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True