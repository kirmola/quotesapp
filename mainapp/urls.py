from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("topics/", views.topics, name="topics"),
    path("topics/<slug:topic_name>/", views.topics, name="topics"),
    path("authors/", views.authors, name="authors"),
    path("authors/<slug:author_name>/", views.authors, name="authors"),
]
