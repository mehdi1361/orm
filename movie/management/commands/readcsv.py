from movie.models import Actor, FilmActor, FilmCategory, Film, Director
from base.models import Category
from django.core.management.base import BaseCommand
from django.utils import timezone
import csv
class Command(BaseCommand):
    help = "read csv actor data"

    def handle(self, *args, **options):
        with open('Movie-Data.csv') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                lst_actor = [Actor.objects.get_or_create(name=x.strip())[0] for x in row[5].split(',')]
                lst_category = [Category.objects.get_or_create(name=x.strip())[0] for x in row[2].split(',')]
                director = Director.objects.get_or_create(name=row[4].strip())[0]
                film = Film.objects.get_or_create(
                    description=row[3].strip(),
                    release_year=row[6],
                    director=director,
                    defaults={'title': row[1].strip()}
                )[0]
                for category in lst_category:
                    FilmCategory.objects.create(category=category, film=film, last_update=timezone.now())

                for actor in lst_actor:
                    FilmActor.objects.create(film=film, actor=actor, last_update=timezone.now())

                print(f"list actor is {lst_actor}, list category : {lst_category}")
