from django.shortcuts import render
from .logics import *
from django.core.paginator import Paginator
from string import ascii_uppercase

# Create your views here.


def authors(request):
    data = getAllAuthors()
    parsedData = {}
    for each in ascii_lowercase:
        parsedData[each] = {k:v for k,v in data if str(v)[0] == each}
    print(parsedData)
    paginator = Paginator(data, 50)
    return render(request, "authors/index.html", {
        "data": parsedData,
        "paginator":paginator,
        # "alphadata": [i for i in ascii_uppercase]
    })


def topics(request):
    data = getAllTopics()
    parsedData = [i for i in data]
    paginator = Paginator(data, 50)
    return render(request, "topics/index.html", {
        "data": parsedData,
        "paginator":paginator
    })
