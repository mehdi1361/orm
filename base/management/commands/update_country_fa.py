from django.core.management.base import BaseCommand
from base.models import Country
from common.utils import get_translate
from django.conf import settings

class Command(BaseCommand):
    help = 'update country fa_name field'

    def handle(self, *args, **kwargs):
        for item in Country.objects.filter(fa_name__isnull=True):
            item.fa_name = get_translate(item.country, settings.TRANSLATE_SOURCE, settings.TRANSLATE_DESTINATION)
            item.save()
            self.stdout.write(f"{item.country}, {item.fa_name}")
