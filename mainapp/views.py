from django.shortcuts import render, redirect
from .logics import *
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import SimpleContactForm
from django.views.decorators.http import require_http_methods

# Create your views here.


def home(request):
    return render(request, "homepage.html")


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
    data = getQuoteAndImages(quote_url)
    fetched_quote = data.quote
    quote_author = data.author
    author_slug = data.author_id
    img1, img2, img3, img4, img5 = data.image_1, data.image_2, data.image_3, data.image_4, data.image_5
    next_five_records = getNextRecordsFromQuotes(quote_url, 5)
    # topics_next_five_records = getNextRecordsInMainAppModels("Topic", )
    return render(request, "quote.html", {
        "quote": fetched_quote,
        "author": quote_author,
        "author_slug" : author_slug,
        "topic_next_five_records": next_five_records[0],
        "author_next_five_records": next_five_records[1],
        "images": [img1, img2, img3, img4, img5]
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