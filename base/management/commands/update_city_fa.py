from base.models import City
from django.core.management import BaseCommand
from common.utils import get_translate
from django.conf import settings
class Command(BaseCommand):
    help = 'update city fname field'

    def handle(self, *args, **options):
        for item in City.objects.filter(fa_name__isnull=True):
            item.fa_name = get_translate(item.city, settings.TRANSLATE_SOURCE, settings.TRANSLATE_DESTINATION)
            item.save()
            self.stdout.write(f"{item.city}, {item.fa_name}")
