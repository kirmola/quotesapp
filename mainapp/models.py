from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from autoslug import AutoSlugField
from shortuuid.django_fields import ShortUUIDField
from django.utils.text import slugify

# Create your models here.


class Quote(models.Model):

    quote = models.CharField(verbose_name="Quote", max_length=250)
    author = models.ForeignKey("mainapp.Author", verbose_name="Author",
                               on_delete=models.CASCADE, to_field="author_slug")
    topics = models.ForeignKey("mainapp.Topic", verbose_name="Topics/Tags",
                               on_delete=models.CASCADE, to_field="topic_slug")
    quote_id = ShortUUIDField(length=6, max_length=45, primary_key=True,
                              alphabet="abcdefghijklmnopqrstuvwxyz123456790", editable=False)
    # image_1 = models.ImageField(verbose_name="Image 1:", upload_to="quoteimg",
    #                             height_field=None, width_field=None, max_length=None, default="default.png")
    # image_2 = models.ImageField(verbose_name="Image 2:", upload_to="quoteimg",
    #                             height_field=None, width_field=None, max_length=None, default="default.png")
    # image_3 = models.ImageField(verbose_name="Image 3:", upload_to="quoteimg",
    #                             height_field=None, width_field=None, max_length=None, default="default.png")
    # image_4 = models.ImageField(verbose_name="Image 4:", upload_to="quoteimg",
    #                             height_field=None, width_field=None, max_length=None, default="default.png")
    # image_5 = models.ImageField(verbose_name="Image 5:", upload_to="quoteimg",
    #                             height_field=None, width_field=None, max_length=None, default="default.png")

    class Meta:

        app_label = "mainapp"
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def save(self, *args, **kwargs):
        fixLenQuote = f"{slugify(self.quote.split()[:4])}-{self.quote_id}"
        self.quote_id = fixLenQuote
        # self.image_1 = f"{fixLenQuote}-1.png"
        # self.image_2 = f"{fixLenQuote}-2.png"
        # self.image_3 = f"{fixLenQuote}-3.png"
        # self.image_4 = f"{fixLenQuote}-4.png"
        # self.image_5 = f"{fixLenQuote}-5.png"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse("Quote_detail", kwargs={"quote_url": self.quote_id})


class Author(models.Model):

    author = models.CharField(verbose_name="Author",
                              max_length=50, unique=True)
    author_slug = AutoSlugField(
        editable=False, populate_from="author", default=None, unique=True)

    class Meta:

        app_label = "mainapp"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"author_name": self.author_slug})


class Topic(models.Model):

    topic = models.CharField(
        "Topics/Tags: ", max_length=50, default=None, unique=True)
    topic_slug = AutoSlugField(
        editable=False, populate_from="topic", default=None, unique=True)

    class Meta:

        app_label = "mainapp"
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("Topic_detail", kwargs={"topic_name": self.topic_slug})


class SimpleContact(models.Model):

    choices = [
        ("problem_in_website", "Regarding Website"),
        ("problem_in_quote", "Regarding Quote"),
        ("problem_in_author", "Regarding Author"),
        ("problem_in_other", "Anything Else"),
    ]

    name = models.CharField(verbose_name="Name", max_length=50)
    email = models.EmailField(verbose_name="Enter Email", max_length=254)
    problem = models.CharField(
        verbose_name="What is the Problem here", choices=choices, max_length=50)
    elaboration = models.TextField(verbose_name="Description")

    class Meta:

        app_label = "mainapp"
        verbose_name = _("SimpleContact")
        verbose_name_plural = _("SimpleContacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SimpleContact_detail", kwargs={"pk": self.pk})
