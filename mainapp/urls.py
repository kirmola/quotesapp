from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("topics/", views.topics, name="topics"),
    path("authors/", views.authors, name="authors"),
    path("<slug:quote_url>/", views.quote, name="Quote_detail"),
    path("topics/<slug:topic_name>/", views.topics, name="Topic_detail"),
    path("authors/<slug:author_name>/", views.authors, name="Author_detail"),
]
