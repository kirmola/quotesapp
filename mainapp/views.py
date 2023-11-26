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
    data = getAllAuthors()
    if author_name:
        reference_dict = {v: k for k, v in data}
        object_list = {i[1] for i in data}
        if author_name in object_list:
            allQuotesByAuthor = getAllQuotesByAuthor(author_name)
            return render(request, "authors/author_individual.html", {
                "author_name": reference_dict[author_name],
                "all_quotes": allQuotesByAuthor
            })
        else:
            raise Http404("No such Author in Database.")
    else:
        parsedData = {}
        for each in ascii_lowercase:
            parsedData[each] = {k: v for k, v in data if str(v)[0] == each}
        paginator = Paginator(data, 50)
        return render(request, "authors/index.html", {
            "data": parsedData,
            "paginator": paginator,
        })


def topics(request, topic_name=None):
    data = getAllTopics()
    if topic_name:
        quotes_collection = getQuotesByTopic(topic_name)
        reference_dict = {v: k for k, v in data}
        object_list = {i[1] for i in data}
        if topic_name in object_list:
            return render(request, "topics/topic_individual.html", {
                "topic_name": reference_dict[topic_name],
                "quotes_collection": quotes_collection
            })
        else:
            raise Http404("No such Topic in Database")
    else:
        parsedData = {}
        for each in ascii_lowercase:
            parsedData[each] = {k: v for k, v in data if str(v)[0] == each}
        paginator = Paginator(data, 50)
        return render(request, "topics/index.html", {
            "data": parsedData,
            "paginator": paginator
        })


def quote(request, quote_url):
    data = getQuote(quote_url)
    fetched_quote = data.quote
    quote_author = data.author
    author_slug = data.author_id
    author_next_five_records = getNextRecordsInMainAppModels("Author", "author_slug", author_slug, 5)
    # topics_next_five_records = getNextRecordsInMainAppModels("Topic", )
    return render(request, "quote.html", {
        "quote": fetched_quote,
        "author": quote_author,
        "author_slug" : author_slug,
        "next_five_authors": author_next_five_records,
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