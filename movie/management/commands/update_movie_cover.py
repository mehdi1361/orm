from django.core.management.base import BaseCommand
from movie.models import Film
import urllib.request
from urllib.parse import quote
from common.utils import Image
import os
from django.core.files import File

class Command(BaseCommand):
    help = 'update movie cover'

    def handle(self, *args, **options):

        for i in Film.objects.all()[:5]:
            b = Image("bing", {"query": i.title, "limit": 1}).find_images_link()
            d = b[0]
            d = quote(d, safe='/:?=&')
            result = urllib.request.urlretrieve(d)
            i.cover.save(os.path.basename(d[0]), File(open(result[0], 'rb')))
