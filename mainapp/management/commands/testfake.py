from faker import Faker
from mainapp.models import *
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from django.conf import settings
# from django.utils.text import slugify


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()




        for _ in range(5):
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

            if (len(quote_text)) < 230:
                current_y_position = 350 if 160 >= len(quote_text) >= 40 else 225
                image = Image.open(f"{settings.BASE_DIR}/staticfiles/images/quote_bg.png")
                font = ImageFont.truetype(f"{settings.BASE_DIR}/staticfiles/fonts/english/Ubuntu-Bold.ttf", size=75)
                # return a list of wrapped text with width setted accordingly
                text_to_write = wrap(quote_text, width=35)
                imageDrawing = ImageDraw.Draw(image)
                for each_piece in text_to_write:
                    imageDrawing.text(font=font, text=each_piece, xy=(
                        330, current_y_position), fill="white")
                    current_y_position += 100
                    fname = f"{slugify(quote_text.split()[:4])}.png"
                    image.save(f"{settings.BASE_DIR}/content/{fname}")
                    quote_instance = Quote.objects.create(quote=quote_text, author=author_instance, topics=topic_instance, image_2=fname)
                    quote_text = fake.sentence(nb_words=30)

                image.close()
            else:
                continue

