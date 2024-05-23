from django.urls import path, include
from . import views
from django.conf.urls import handler404
from .views import *
from mainapp.distill import (get_authors, get_quotes, get_topics, get_author_paginator, get_topic_paginator, get_alphabets)
from django_distill import distill_path

handler404 = "mainapp.views.custom404"

urlpatterns = [
    distill_path("", HomeView.as_view(), name="home"),
    distill_path("featured-quote/", Qotd.as_view(), name="qotd"),
    distill_path("topics/", TopicListView.as_view(), name="topics"),
    distill_path("authors/starts-with-<str:alphabet>/", AuthorListView.as_view(), name="authors_by_alphabet", distill_func=get_alphabets),
    distill_path("topics/<slug:topic_name>/", TopicDetailView.as_view(), name="Topic_detail", distill_func=get_topics),
    distill_path("topics/<slug:topic_name>/page/<int:page>/", TopicDetailView.as_view(), name="topic_paginator", distill_func=get_topic_paginator),
    distill_path("authors/<slug:author_name>/", QuoteDetailView.as_view(), name="Author_detail",distill_func=get_authors),
    distill_path("authors/<slug:author_name>/page/<int:page>/", QuoteDetailView.as_view(), name="author_paginator", distill_func=get_author_paginator),
    distill_path("contact/", views.contact, name="contact"),
    # path("search/", views.search, name="search"),
    # path("thanks-for-contacting/", views.thanks_for_contacting, name="thanks_for_contacting"),
    distill_path("<slug:quote_url>/", QuoteView.as_view(), name="Quote_detail", distill_func=get_quotes),
]