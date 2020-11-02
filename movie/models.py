from django.db import models
from base.models import Base, Language, Category
from django.utils import timezone
from django.db import connection

class Film(Base):
    RATING_CHOICES = [('R', 'R'), ('PG-13', 'PG-13'), ('NC-17', 'NC-17')]
    title = models.CharField(max_length=30, db_index=True)
    description = models.TextField()
    release_year = models.SmallIntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    rental_duration = models.SmallIntegerField(default=3)
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2, default=4.99)
    length = models.SmallIntegerField()
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2, default=19.99)
    rating = models.CharField(max_length=5, choices=RATING_CHOICES, default='R')
    last_update = models.DateTimeField()
    cover = models.ImageField(upload_to='media/cover', null=True)
    category = models.ManyToManyField(Category, through="FilmCategory")
    fa_title = models.CharField(max_length=100, null=True)
    fa_description = models.TextField(null=True)

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        self.language = 1
        super(Film, self).save(*args, **kwargs)

    class Meta:
        db_table = 'movie_film'
        ordering = ['last_update']

    def __str__(self):
        return self.title

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))


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

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))

class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "movie_film_actor"
        ordering = ["last_update"]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))


class FilmCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "movie_film_category"
        ordering = ["last_update"]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))
