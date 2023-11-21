from .models import *


def getAllAuthors():
    queryset = Author.objects.all()
    return queryset


def getAllTopics():
    queryset = Topic.objects.all()
    return queryset
