from .models import *
from django.core.paginator import Paginator


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
    pagination = Paginator(topics, 15)
    page_range = pagination.num_pages
    for topic in topics:
        for page_num in range(page_range):
            yield {
                "topic_name":topic.topic_slug,
                "page":page_num,
            }
    


def get_author_paginator():
    authors = Author.objects.all()
    pagination = Paginator(author, 15)
    page_range = pagination.num_pages
    for author in authors:
        for page_num in page_range:
            yield {
                "author_name":author.author_slug,
                "page":page_num,
            }



def get_sitemap_index():
    keys = ["quote", "author", "topic"]
    for each in keys:
        yield {
            "section":each
        }


def get_sitemap():
    pass