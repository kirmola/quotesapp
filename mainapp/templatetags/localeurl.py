from django import template
from django.urls import translate_url

register = template.Library()

@register.simple_tag
def translateURL(url, langcode):
    return translate_url(url, langcode)
