from .models import *
from string import ascii_lowercase
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.apps import apps
from string import ascii_lowercase


def getAllAuthors():
    newqset = []
    for each in ascii_lowercase:
        queryset = Author.objects.filter(author_slug__startswith=each).values_list("author", "author_slug")[:10]
        newqset.extend(queryset)
    return newqset


def getTopics(limit:int):
    newqset = []
    for each in ascii_lowercase:
        queryset = Topic.objects.filter(topic_slug__startswith=each).values_list("topic", "topic_slug")[:limit]
        newqset.extend(queryset)
    return newqset


def getQuoteAndImages(quote_url):
    queryset = get_object_or_404(Quote, quote_id=quote_url)
    return queryset

def getAllQuotesByAuthor(author_name):
    queryset = Quote.objects.filter(author=author_name).values_list("quote", "quote_id")
    return queryset

def getQuotesByTopic(topic_name):
    queryset = Quote.objects.filter(topics_id=topic_name).values("quote", "quote_id")
    return queryset

def getNextRecordsFromQuotes(current_url, how_many_records_needed:int):
    master_qset = Quote.objects.filter(quote_id__gt=current_url).values_list("author_id", "topics_id")[how_many_records_needed:how_many_records_needed+5]
    topics_qset = [Topic.objects.filter(topic_slug=i[1]).values_list("topic", "topic_slug") for i in master_qset]
    author_qset = [Author.objects.filter(author_slug=i[0]).values_list("author", "author_slug") for i in master_qset]
    return topics_qset, author_qset
    

def verifyAuthor(author_in_url):
    qset = get_object_or_404(Author, author_slug=author_in_url)
    if qset:
        return True
    return False

def verifyTopic(topic_in_url):
    qset = get_object_or_404(Topic, topic_slug=topic_in_url)
    return 

def getTopicTitle(topic_slug):
    qset = Topic.objects.filter(topic_slug=topic_slug)
    return qset