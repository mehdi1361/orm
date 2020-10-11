from django.db import models
from base.models import Base, Language
import tsvector_field
from django.utils import timezone

class Film(Base):
    YEAR_IN_SCHOOL_CHOICES = [('R', 'R'), ('PG-13', 'PG-13'), ('NC-17', 'NC-17')]
    title = models.CharField(max_length=30, db_index=True)
    description = models.TextField()
    release_year = models.SmallIntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    rental_duration = models.SmallIntegerField(default=3)
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2, default=4.99)
    length = models.SmallIntegerField()
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2, default=19.99)
    rating = models.CharField(max_length=5, choices=YEAR_IN_SCHOOL_CHOICES)
    last_update = models.DateTimeField()
    special_features = models.TextField()
    fulltext = tsvector_field.SearchVectorField()
    cover = models.ImageField(upload_to='media/cover', null=True)

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(Film, self).save(*args, **kwargs)

    class Meta:
        db_table = 'movie_film'
        ordering = ['last_update']

    def __str__(self):
        return self.title


class Actor(Base):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_update = models.DateTimeField()
    film = models.ManyToManyField(Film, through="FilmActor")

    class Meta:
        db_table = "movie_actor"
        ordering = ["last_update"]

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "movie_film_actor"
        ordering = ["last_update"]
