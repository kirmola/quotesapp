from faker import Faker
from mainapp.models import *
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
# from django.utils.text import slugify


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()




        for _ in range(50):
            # Create or retrieve an Author instance
            author_name = fake.name()
            author_instance, _ = Author.objects.get_or_create(author=author_name)

            # Create or retrieve a Topic instance
            topic_name = fake.word()
            topic_instance, _ = Topic.objects.get_or_create(topic=topic_name)

            email = fake.email()
            SimpleContact.objects.get_or_create(name=author_name, email=email, problem="problem_in_other", elaboration=fake.sentence(nb_words=100))
            # Create a Quote instance
            quote_text = fake.sentence(nb_words=30)

            fname = f"{slugify(quote_text.split()[:4])}.png"
            quote_instance = Quote.objects.create(quote=quote_text, author=author_instance, topics=topic_instance)
