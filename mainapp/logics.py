from .models import *
from string import ascii_lowercase
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.apps import apps
from string import ascii_lowercase
from random import randint

def getAllAuthors():
    newqset = []
    for each in ascii_lowercase:
        queryset = Author.objects.filter(author_slug__startswith=each).values_list("author", "author_slug")[:10]
        newqset.extend(queryset)
    return newqset


def getTopics(limit:int, where_to_display=None):
    if where_to_display and where_to_display == "homepage":
        newqset = Topic.objects.values_list("topic", "topic_slug")[:limit]
        return newqset
    else:
        newqset = []
        for each in ascii_lowercase:
            queryset = Topic.objects.filter(topic_slug__startswith=each).values_list("topic", "topic_slug")[:limit]
            newqset.extend(queryset)
        return newqset


def getQuoteData(quote_url, limit_next_records:int):
    qobj = Quote.objects
    qdataset = qobj.filter(quote_id=quote_url)
    quote_data = qdataset.values_list("quote", "author", "author__author", "topics", "image_1", "image_2", "image_3", "image_4", "image_5",).get()
    
    random_quotes = qobj.filter(quote_id__gt=quote_url).values_list("quote", "author", "author__author", "quote_id")[:14]
    authors_data = qobj.filter(quote_id__gt=quote_url).values("author","author__author")[:limit_next_records]
    topics_data = qobj.filter(quote_id__gt=quote_url).values("topics","topics__topic")[:limit_next_records]
    
    return authors_data, topics_data, quote_data, random_quotes

def getQuotesByAuthor(author_name):
    queryset = Quote.objects.filter(author=author_name).values_list("quote", "quote_id")
    return queryset

def getQuotesByTopic(topic_name):
    queryset = Quote.objects.filter(topics_id=topic_name).values("quote", "quote_id")
    return queryset    

def verifyAuthor(author_in_url):
    qset = get_object_or_404(Author, author_slug=author_in_url)
    return

def verifyTopic(topic_in_url):
    qset = get_object_or_404(Topic, topic_slug=topic_in_url)
    return 

def getTopicTitle(topic_slug):
    qset = Topic.objects.filter(topic_slug=topic_slug)
    return qset

def getAuthorTitle(author_name):
    qset = Author.objects.filter(author_slug=author_name)
    return qset

def getAuthors(limit:int, where_to_display=None):
    if where_to_display and where_to_display == "homepage":
        newqset = Author.objects.values_list("author", "author_slug")[:limit]
        return newqset
    else:
        newqset = []
        for each in ascii_lowercase:
            queryset = Author.objects.filter(author_slug__startswith=each).values_list("author", "author_slug")[:limit]
            newqset.extend(queryset)
        return newqset

def verifyQuoteURL(quote_url):
    qset = get_object_or_404(Quote, quote_id=quote_url)

def getQuoteOfTheDay():
    obj = Quote.objects
    total_records = len(obj.all())
    random_number = randint(0, total_records)
    print(random_number)
    queryset = obj.values_list("quote", "author", "author__author", "topics")[random_number:random_number+10]
    return queryset


def fetchSearchData(searchTerm, number_of_results):
    qset = Quote.objects.filter(quote__contains=searchTerm).values_list("quote", "quote_id", "topics", "topics_id")[:number_of_results]
    return qset