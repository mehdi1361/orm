from django.core.management.base import BaseCommand
from movie.models import Film
import urllib.request
from urllib.parse import quote
from common.utils import Image
import os
from django.core.files import File


def save_image(obj, lst_images):
    for image in lst_images:
        try:
            d = quote(image, safe='/:?=&')

            result = urllib.request.urlretrieve(d)
            obj.cover.save(os.path.basename(str(image).split("/")[-1]), File(open(result[0], 'rb')))
            print(f"save image for {obj.title}")
            return
        except d:
            pass


class Command(BaseCommand):
    help = 'update movie cover'

    def handle(self, *args, **options):

        for i in Film.objects.filter(cover=""):
            images = Image("bing", {"query": f"{i.title} {i.release_year} movie cover", "limit": 3}).find_images_link()
            save_image(i, images)
