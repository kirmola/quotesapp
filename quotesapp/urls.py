"""
URL configuration for quotesapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from quotesapp import views
from django.contrib.sitemaps.views import sitemap, index
from mainapp.sitemaps import *
from django.conf.urls.i18n import i18n_patterns
from django_distill import distill_path
from mainapp.distill import (get_sitemap_index)


sitemaps={
    "quote":QuoteSitemap,
    "topic":TopicSitemap,
    "author":AuthorSitemap,
}


urlpatterns = [
    distill_path("robots.txt", views.robots, name="robots"),
    path('admin/', admin.site.urls),
    distill_path("sitemap.xml", index, {"sitemaps":sitemaps}, name="django.contrib.sitemaps.views.index"),
    distill_path("sitemap-<section>.xml", sitemap, {"sitemaps":sitemaps}, name="django.contrib.sitemaps.views.sitemap", distill_func=get_sitemap_index),
    path("", include("mainapp.urls"))
]

# urlpatterns += i18n_patterns(
#     path("", include("mainapp.urls")),
# )
