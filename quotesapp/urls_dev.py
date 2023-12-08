from .urls import *
from django.conf.urls import static
from django.conf import settings


urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    ]+static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
