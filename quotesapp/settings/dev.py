from quotesapp.base_settings import *

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS+=[
    "debug_toolbar",
]

MIDDLEWARE+=[
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True