from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse

class QuoteSitemap(Sitemap):
    
    def items(self):
        return Quote.objects.all()

class AuthorSitemap(Sitemap):
    
    def items(self):
        return Author.objects.all()

class TopicSitemap(Sitemap):

    def items(self):
        return Topic.objects.all()
    

# class SitemapIndex(Sitemap):
    
#     def items(self):
#         return [Quote.objects.all(), Author.objects.all(), Topic.objects.all()]
    
#     def location(self, item):
#         return item.get_absolute_url()