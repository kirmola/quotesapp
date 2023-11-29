from quotesapp.base_settings import *

SITE_NAME = "QuotesApp"


ALLOWED_HOSTS = ["*"]

INSTALLED_APPS+=[
    "debug_toolbar",
    "django_browser_reload",
]

MIDDLEWARE+=[
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True