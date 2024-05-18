from django.urls import path, include
from . import views
from django.conf.urls import handler404
from .views import *


handler404 = "mainapp.views.custom404"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("quote-of-the-day/", views.qotd, name="qotd"),
    path("topics/", TopicListView.as_view(), name="topics"),
    path("authors/", AuthorListView.as_view(), name="authors"),
    path("quote/<slug:quote_url>/", views.quote, name="Quote_detail"),
    path("topics/<slug:topic_name>/", QuoteListOnTopicView.as_view(), name="Topic_detail"),
    path("authors/<slug:author_name>/", QuoteListOnAuthorView.as_view(), name="Author_detail"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("thanks-for-contacting/", views.thanks_for_contacting, name="thanks_for_contacting"),
]