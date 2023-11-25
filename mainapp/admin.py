from django.contrib import admin
from .models import *

# Register your models here.

class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ("name", "email", "problem", "elaboration")
admin.site.register([Quote, Author, Topic])

admin.site.register(SimpleContact, ReadOnlyFields)