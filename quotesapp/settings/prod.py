from quotesapp.base_settings import *
import dj_database_url

ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = 'quotesapp.urls'

SITE_NAME = "Quoteshrine"

INSTALLED_APPS+=[

]

MIDDLEWARE+=[

]

# DATABASES = {
#         'default': dj_database_url.parse("postgres://postgres:root@localhost:5432/quotesapp")
#     }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "quotesdb.sqlite3",
    }
}

DEBUG = False
