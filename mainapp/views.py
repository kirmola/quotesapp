from django.shortcuts import render, redirect
from .logics import *
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import SimpleContactForm
from django.views.decorators.http import require_http_methods

# Create your views here.


def home(request):
    topics = getTopics(10, "homepage")
    authors = getAuthors(10, "homepage")
    return render(request, "homepage.html", {
        "topics":topics,
        "authors":authors
    })


def authors(request, author_name=None):
    if author_name:
        verifyAuthor(author_name)
        quotes_collection = getQuotesByAuthor(author_name)
        author_name = getAuthorTitle(author_name)
        return render(request, "authors/author_individual.html", {
            "quotes_collection": quotes_collection,
            "author_name": author_name[0],
        })
    else:
        data = getAuthors(10)
        parsedData = {each:{k:v for k,v in data if str(v)[0] == each} for each in ascii_lowercase}
        return render(request, "authors/index.html", {
            "data": parsedData,
        })


def topics(request, topic_name=None):
    if topic_name:
        verifyTopic(topic_name)
        quotes_collection = getQuotesByTopic(topic_name)
        topic_name = getTopicTitle(topic_name)
        return render(request, "topics/topic_individual.html", {
            "topic_name": topic_name[0],
            "quotes_collection": quotes_collection
        })
    else:
        data = getTopics(10)
        parsedData = {each:{k:v for k,v in data if str(v)[0] == each} for each in ascii_lowercase}
        return render(request, "topics/index.html", {
            "data": parsedData,
        })


def quote(request, quote_url):
    verifyQuoteURL(quote_url)
    data = getQuoteData(quote_url, 10)
    quote_data = data[2]
    author_data = [i for i in data[0]]
    topic_data = [j for j in data[1]]
    random_quotes = [k for k in data[3]]
    images = [quote_data[5], quote_data[6], quote_data[7], quote_data[8]]
    thumbs = [str(i).removesuffix(".png").__add__("-thumb.png") for i in images]

    return render(request, "quote.html", {
        "quote":quote_data[0],
        "author":quote_data[1],
        "topic":quote_data[2],
        "author_title":quote_data[2],
        "images" : zip(images,thumbs),
        "main_image":quote_data[4],
        "authors_data":author_data,
        "topics_data":topic_data,
        "random_quotes":random_quotes
    })


@require_http_methods(["GET", "POST"])
def contact(request):

    method = request.method

    match(method):
        case "GET":
            form = SimpleContactForm()
            return render(request, "pages/contact.html", {
                "form": form,
            })
        case "POST":
            formData = SimpleContactForm(request.POST)
            ack = formData.save()
            return HttpResponseRedirect("/thanks-for-contacting/")


def thanks_for_contacting(request):
    return render(request, "ack.html")


def custom404(request, exception):
    return render(request, "404.html", status=404)


def qotd(request):
    data = getQuoteOfTheDay()
    return render(request, "qotd.html", {
        "data":[i for i in data]
    })