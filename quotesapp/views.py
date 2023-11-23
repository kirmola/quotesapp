from django.shortcuts import render

def robots(request):
    return render(request, content_type="text/plain", template_name="robots.txt")