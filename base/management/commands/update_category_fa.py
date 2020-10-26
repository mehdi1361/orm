from base.models import Category
from django.core.management.base import BaseCommand
from common.utils import get_translate
from django.conf import settings

class Command(BaseCommand):
    help = 'update category fa_name field'

    def handle(self, *args, **options):
        for item in Category.objects.filter(fa_name__isnull=True):
            item.fa_name = get_translate(item.name, settings.TRANSLATE_SOURCE, settings.TRANSLATE_DESTINATION)
            item.save()
            self.stdout.write(f"{item.name},{item.fa_name}")
