from .models import *
from django.core.paginator import Paginator, Page


def get_quotes():
    quotes = Quote.objects.all()
    for each in quotes:
        yield {
            "quote_url":each.quote_id
        }


def get_authors():
    authors = Author.objects.all()
    for each in authors:
        yield {
            "author_name":each.author_slug
        }


def get_topics():
    topics = Topic.objects.all()
    for each in topics:
        yield {
            "topic_name":each.topic_slug
        }


def get_topic_paginator():
    topics = Topic.objects.all()
    data = {
        str(topic.topic_slug): Paginator(Quote.objects.filter(topics=topic), 15).page_range for topic in topics
    }        
    
    for k, v in data.items():
        for each in v:
            yield {
                "topic_name":k,
                "page":each,
            }
    


def get_author_paginator():
    authors = Author.objects.all()
    data = {
        str(author.author_slug) : Paginator(Quote.objects.filter(author=author), 15).page_range for author in authors
    }

    for k, v in data.items():
        for each in v:
            yield {
                "author_name":k,
                "page":each,
            }



def get_sitemap_index():
    keys = ["quote", "author", "topic"]
    for each in keys:
        yield {
            "section":each
        }


def get_sitemap():
    pass