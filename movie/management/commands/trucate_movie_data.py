from movie.models import Actor, FilmActor, FilmCategory, Film
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'truncate the Film, FilmCategory, FilmActor, Actor'

    def handle(self, *args, **options):
        Film.truncate()
        FilmActor.truncate()
        FilmCategory.truncate()
        Actor.truncate()
        self.stdout.write(f'delete {Film} {FilmActor} {FilmCategory} {Actor} database')
