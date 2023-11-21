from django.shortcuts import render
from .logics import *
from django.core.paginator import Paginator

# Create your views here.


def authors(request):
    data = getAllAuthors()
    parsedData = [i for i in data]
    paginator = Paginator(data, 50)
    return render(request, "authors/index.html", {
        "data": parsedData,
        "paginator":paginator
    })


def topics(request):
    data = getAllTopics()
    parsedData = [i for i in data]
    paginator = Paginator(data, 50)
    return render(request, "topics/index.html", {
        "data": parsedData,
        "paginator":paginator
    })
