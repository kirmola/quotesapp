from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from os.path import exists

from faker import Faker
from mainapp.models import *
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from django.conf import settings


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        fake = Faker()

        queryset = Quote.objects.values_list("quote", "quote_id")
        quotes = [i[0] for i in queryset]
        filenames = [i[1] for i in queryset]

        for quote, filename in zip(quotes, filenames):
            if (len(quote)) < 230:
                current_y_position = 350 if 160 >= len(quote) >= 40 else 225
                image = Image.open(f"{settings.BASE_DIR}/staticfiles/images/quote_bg.png")
                font = ImageFont.truetype(f"{settings.BASE_DIR}/staticfiles/fonts/english/Ubuntu-Bold.ttf", size=75)
                # return a list of wrapped text with width setted accordingly
                text_to_write = wrap(quote, width=35)
                imageDrawing = ImageDraw.Draw(image)
                qset = Quote.objects
                for each_piece in text_to_write:
                    imageDrawing.text(font=font, text=each_piece, xy=(
                        330, current_y_position), fill="white")
                    current_y_position += 100
                    image_name = f"{filename}.png"
                save_location = f"{settings.MEDIA_ROOT}"
                if exists(f"{save_location}/{image_name}"):
                    self.stdout.write("Image is already there. No need to save.")
                else:
                    image.save(f"{save_location}/{image_name}")
                qset.filter(quote_id=filename).update(image_1=image_name)

                image.close()
            else:
                continue
