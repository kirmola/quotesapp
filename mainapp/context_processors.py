from django.conf import settings

def getSiteName(request):
    return {"SITE_NAME":settings.SITE_NAME}