import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from os.path import exists, join
from faker import Faker
from mainapp.models import Quote
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        fake = Faker()

        queryset = Quote.objects.values_list("quote", "quote_id")
        quotes = [i[0] for i in queryset]
        filenames = [i[1] for i in queryset]
        print(len(quotes), len(filenames))
        bg_image_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'images')
        bg_images_list = [join(bg_image_path, imagefile) for _, _, files in os.walk(bg_image_path) for imagefile in files]

        thumbnail_size = (96,54)
        image_save_location = settings.MEDIA_ROOT

        with ThreadPoolExecutor(max_workers=1000) as executor:
            futures = []

            for quote, filename in zip(quotes, filenames):
                imgobj = [Image.open(i) for i in bg_images_list]
                font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'staticfiles', 'fonts', 'english', 'Ubuntu-Bold.ttf'), size=75)

                for index, each in enumerate(imgobj):
                    futures.append(
                        executor.submit(self.process_image, each, quote, filename, index, font, thumbnail_size, image_save_location)
                    )

            for future in as_completed(futures):
                # Retrieve the result of each completed future (even though the function doesn't return anything)
                future.result()

    def process_image(self, img, quote, filename, index, font, thumbnail_size, image_save_location):
        imageDrawing = ImageDraw.Draw(img)
        current_y_position = 300 if 160 >= len(quote) >= 40 else 225
        text_to_write = wrap(quote, width=40)

        for each_piece in text_to_write:
            imageDrawing.text(font=font, text=each_piece, xy=(250, current_y_position), stroke_fill="black", stroke_width=5, fill="white")
            current_y_position += 100

        image_name = f"{filename}-{index + 1}.png"
        thumbnail_name = f"{filename}-{index + 1}-thumb.png"

        if exists(join(image_save_location, image_name)):
            self.stdout.write("Image is already there. No need to save.")
        else:
            img.save(join(image_save_location, image_name), optimize=True)

            # Thumbnail is being saved at this point
            # Just remove image_save_location and put thumbnail_save_location below if you want thumbnails to be saved in a new location
            img.thumbnail(thumbnail_size)
            img.save(join(image_save_location, thumbnail_name), optimize=True)

            self.stdout.write(f"'{image_name}' has been saved successfully.")
