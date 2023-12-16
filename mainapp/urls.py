from django.urls import path, include
from . import views
from django.conf.urls import handler404

handler404 = "mainapp.views.custom404"

urlpatterns = [
    path("", views.home, name="home"),
    path("quote-of-the-day/", views.qotd, name="qotd"),
    path("topics/", views.topics, name="topics"),
    path("authors/", views.authors, name="authors"),
    path("quote/<slug:quote_url>/", views.quote, name="Quote_detail"),
    path("topics/<slug:topic_name>/", views.topics, name="Topic_detail"),
    path("authors/<slug:author_name>/", views.authors, name="Author_detail"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("thanks-for-contacting/", views.thanks_for_contacting, name="thanks_for_contacting"),
]