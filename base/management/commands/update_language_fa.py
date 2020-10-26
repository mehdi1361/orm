from base.models import Language
from common.utils import get_translate
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'update language fname field'

    def handle(self, *args, **options):
        for item in Language.objects.filter(fa_name__isnull=True):
            item.fa_name = get_translate(item.name, settings.TRANSLATE_SOURCE, settings.TRANSLATE_DESTINATION)
            item.save()
            self.stdout.write(f"{item.name},{item.fa_name}")
