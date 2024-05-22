from django.shortcuts import render, redirect
from .logics import *
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import SimpleContactForm
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView
from .models import *


class HomeView(ListView):
    template_name = "homepage.html"


    def get_queryset(self):

        top_10_authors = Author.objects.all()[:10].values("author", "author_slug")
        top_10_topics = Topic.objects.all()[:10].values("topic", "topic_slug")


        return (top_10_authors, top_10_topics)
    

class TopicListView(ListView):
    template_name = "topics/index.html"
    queryset = Topic.objects.all().values("topic", "topic_slug")


class AuthorListView(ListView):
    template_name = "authors/index.html"
    queryset = Author.objects.all().values("author", "author_slug")
    

class QuoteView(DetailView):
    model = Quote
    template_name = "quote.html"
    slug_field = "quote_id"
    
    slug_url_kwarg = "quote_url"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.order_by("?").all()[:10]
        context["authors"] = Author.objects.order_by("?").all()[:10]
        context["quotes"] = Quote.objects.order_by("?").all()[:12]
        return context
    

class TopicDetailView(ListView):
    model = Quote
    template_name = "topics/topic_individual.html"
    slug_field = "topics"
    slug_url_kwarg = "topic_name"
    paginate_by = 15


    


    def get_queryset(self):
        return super().get_queryset().filter(topics__topic_slug=self.kwargs.get("topic_name")).values("quote", "quote_id").all()    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_topic"] = super().get_queryset().filter(topics__topic_slug=self.kwargs.get("topic_name")).distinct().values("topics__topic", "topics").get()
        return context
        

class QuoteDetailView(ListView):
    model = Quote
    template_name = "authors/author_individual.html"
    slug_field = "author"
    slug_url_kwarg = "author_name"
    paginate_by = 15


    def get_queryset(self):
        return super().get_queryset().filter(author__author_slug=self.kwargs.get("author_name")).values("quote", "quote_id").all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_author"] = Author.objects.filter(author_slug=self.kwargs.get("author_name")).values("author", "author_slug").get()
        return context


class Qotd(ListView):
    template_name = "qotd.html"
    model = Quote
    queryset = Quote.objects.order_by("?").first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra_quotes"] = Quote.objects.order_by("?").values("quote", "quote_id","author__author", "topics__topic", "author", "topics").all()[:10]
        return context
    


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
            formData.save()
            return HttpResponseRedirect("/thanks-for-contacting/")


def thanks_for_contacting(request):
    return render(request, "ack.html")


def custom404(request, exception):
    return render(request, "404.html", status=404)


@require_http_methods(["GET"])
def search(request):
    searchTerm = request.GET["search_term"]
    number_of_results = 10
    results = fetchSearchData(searchTerm, number_of_results)
    return render(request, "search.html", {
        "results":results
    })
