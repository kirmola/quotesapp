from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from autoslug import AutoSlugField

# Create your models here.

class Quote(models.Model):

    quote = models.CharField(_("Quote"), max_length=250)
    author = models.ForeignKey("mainapp.Author", verbose_name=_("Author"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Quote")
        verbose_name_plural = _("Quotes")

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse("Quote_detail", kwargs={"pk": self.pk})


class Author(models.Model):

    author = models.CharField(_("Author: "), max_length=50)
    author_slug = AutoSlugField(editable=False, populate_from="author", default=None)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})
