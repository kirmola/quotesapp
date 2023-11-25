from .models import *
from string import ascii_lowercase
from django.shortcuts import get_object_or_404
from django.db.models import Q
from string import ascii_lowercase


def getAllAuthors():
    queryset = []
    for each in ascii_lowercase:
        query = Q(author_slug__startswith=each)
        data  = Author.objects.filter(query).values_list("author", "author_slug")[:10]
        queryset.extend(data)
    return queryset


def getAllTopics():
    queryset = []
    for each in ascii_lowercase:
        query = Q(topic_slug__startswith=each)
        data = Topic.objects.filter(query).values_list("topic", "topic_slug")[:10]
        queryset.extend(data)
    return queryset


def getQuote(quote_url):
    queryset = get_object_or_404(Quote, quote_id=quote_url)
    return queryset

def getAllQuotesByAuthor(author_name):
    queryset = Quote.objects.filter(author=author_name).values_list("quote", "quote_id")
    return queryset

def getQuotesByTopic(topic_name):
    queryset = Quote.objects.filter(topics_id=topic_name).values("quote", "quote_id")
    return queryset