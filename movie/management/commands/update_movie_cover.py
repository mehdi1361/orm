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
        # i = Image("bing", {"query": "Rogue One", "limit": 1}).find_images_link()
        # d = i[0]
        # d = quote(d, safe='/:?=&')
        # s = Film.objects.get(title='Rogue One')
        # result = urllib.request.urlretrieve(d)
        # s.cover.save(os.path.basename(d[0]), File(open(result[0], 'rb')))


        for  i in Film.objects.all()[:5]:
            b = Image("bing", {"query": i.title, "limit": 1}).find_images_link()
            d = b[0]
            d=quote(d, safe='/:?=&')
            result = urllib.request.urlretrieve(d)
            i.cover.save(os.path.basename(d[0]), File(open(result[0], 'rb')))





        # s.cover.save()


c = Command()
c.handle()








