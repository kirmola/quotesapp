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


def getAllTopics():
    newqset = []
    for each in ascii_lowercase:
        queryset = Topic.objects.filter(topic_slug__startswith=each).values_list("topic", "topic_slug")[:10]
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

def getNextRecordsInMainAppModels(model, field_name, field_value ,required_records:int):
    qsetmodel =  apps.get_model(app_label="mainapp", model_name=model)
    
    record_number = qsetmodel.objects.filter(**{field_name:field_value}).values("id").get()["id"]
    next_records = qsetmodel.objects.filter(id__gt=record_number)[:required_records]
    return next_records
    