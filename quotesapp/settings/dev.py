from quotesapp.base_settings import *
import dj_database_url

SITE_NAME = "QuotesApp"


ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = 'quotesapp.urls_dev'


INSTALLED_APPS+=[
    "debug_toolbar",
    "django_browser_reload",
]

MIDDLEWARE+=[
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "quotes.sqlite3",
    }
}

DEBUG = True



NPM_BIN_PATH = "C:\\Program Files\\nodejs\\npm.cmd"