from .models import *
from string import ascii_lowercase

def getAllAuthors():
    queryset = Author.objects.values_list("author", "author_slug")
    return queryset


def getAllTopics():
    queryset = Topic.objects.values_list("topic", "topic_slug")
    return queryset
