from django.shortcuts import render
from .logics import *
from django.core.paginator import Paginator

# Create your views here.


def authors(request, author_name=None):
    data = getAllAuthors()
    reference_dict = {v:k for k,v in data}
    object_list = {i[1] for i in data}
    if author_name in object_list:
        return render(request, "authors/author_individual.html", {
            "author_name":reference_dict[author_name]
        })
    else:
        parsedData = {}
        for each in ascii_lowercase:
            parsedData[each] = {k:v for k,v in data if str(v)[0] == each}
        paginator = Paginator(data, 50)
        return render(request, "authors/index.html", {
            "data": parsedData,
            "paginator":paginator,
        })


def topics(request, topic_name=None):
    data = getAllTopics()
    reference_dict = {v:k for k,v in data}
    object_list = {i[1] for i in data}
    if topic_name in object_list:
        return render(request, "topics/topic_individual.html", {
            "topic_name":reference_dict[topic_name]
        })
    else:
        parsedData = {}
        for each in ascii_lowercase:
            parsedData[each] = {k:v for k,v in data if str(v)[0]==each}
        paginator = Paginator(data, 50)
        return render(request, "topics/index.html", {
            "data": parsedData,
            "paginator":paginator
        })
