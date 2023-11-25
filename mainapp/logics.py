from .models import *
from string import ascii_lowercase
from django.shortcuts import get_object_or_404

def getAllAuthors():
    queryset = Author.objects.values_list("author", "author_slug")
    return queryset


def getAllTopics():
    queryset = Topic.objects.values_list("topic", "topic_slug")

    return queryset


def getQuote(quote_url):
    queryset = get_object_or_404(Quote, quote_id=quote_url)
    return queryset

def getAllQuotesByAuthor(author_name):
    queryset = Quote.objects.filter(author=author_name).values_list("quote", "quote_id")
    return queryset