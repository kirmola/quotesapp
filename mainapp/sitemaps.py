from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse

class QuoteSitemap(Sitemap):
    
    i18n = True
    
    limit = 50000

    def items(self):
        return Quote.objects.all()

class AuthorSitemap(Sitemap):
    
    i18n = True
    
    limit = 50000

    def items(self):
        return Author.objects.all()

class TopicSitemap(Sitemap):

    i18n = True
    
    limit = 50000

    def items(self):
        return Topic.objects.all()