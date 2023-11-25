from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("topics/", views.topics, name="topics"),
    path("authors/", views.authors, name="authors"),
    path("quote/<slug:quote_url>/", views.quote, name="Quote_detail"),
    path("topics/<slug:topic_name>/", views.topics, name="Topic_detail"),
    path("authors/<slug:author_name>/", views.authors, name="Author_detail"),
    path("contact/", views.contact, name="contact"),
    path("thanks-for-contacting/", views.thanks_for_contacting, name="thanks_for_contacting"),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    