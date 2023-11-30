from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from os.path import exists, abspath
from os import listdir, walk
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
        bg_image_path = f"{settings.BASE_DIR}/staticfiles/images/"
        bg_images_list = []


        for files in walk(bg_image_path):
            imagefiles_in_dir = files[2]
            for imagefile in imagefiles_in_dir:
                bg_images_list.append(f"{bg_image_path}{imagefile}")


        for quote, filename in zip(quotes, filenames):
            if (len(quote)) < 230:
                imgobj = [Image.open(i) for i in bg_images_list]
                font = ImageFont.truetype(f"{settings.BASE_DIR}/staticfiles/fonts/english/Ubuntu-Bold.ttf", size=75)

                for each in enumerate(imgobj):
                    imageDrawing = ImageDraw.Draw(each[1])

                    current_y_position = 300 if 160 >= len(quote) >= 40 else 225
                    text_to_write = wrap(quote, width=40)
                    for each_piece in text_to_write:
                        imageDrawing.text(font=font, text=each_piece, xy=(
                            250, current_y_position), stroke_fill="black", stroke_width=5,fill="white")
                        current_y_position += 100
                        image_name = f"{filename}-{each[0]+1}.png"
                    save_location = f"{settings.MEDIA_ROOT}"
                    if exists(f"{save_location}/{image_name}"):
                        self.stdout.write("Image is already there. No need to save.")
                    else:
                        each[1].save(f"{save_location}/{image_name}")
                    

                    
                    each[1].close()
            else:
                continue
