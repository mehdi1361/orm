from django.db import models
from base.models import Base, Language, Category
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Avg

class Director(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'movie_director'

    def __str__(self):
        return self.name

class Film(Base):
    RATING_CHOICES = [
        ('R', 'R'),
        ('PG-13', 'PG-13'),
        ('NC-17', 'NC-17')
    ]

    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    release_year = models.SmallIntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    rental_duration = models.SmallIntegerField(default=3)
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2, default=4.99)
    length = models.SmallIntegerField(null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2, default=19.99)
    rating = models.CharField(max_length=5, choices=RATING_CHOICES, default='R')
    last_update = models.DateTimeField()
    cover = models.ImageField(upload_to='media/cover', null=True)
    category = models.ManyToManyField(Category, through="FilmCategory")
    fa_title = models.CharField(max_length=100, null=True)
    fa_description = models.TextField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        self.language = Language.objects.get(pk=1)
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
    name = models.CharField(max_length=100, unique=True)
    last_update = models.DateTimeField()
    film = models.ManyToManyField(Film, through="FilmActor")

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(Actor, self).save(*args, **kwargs)

    class Meta:
        db_table = "movie_actor"
        ordering = ["last_update"]

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))

class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(FilmActor, self).save(*args, **kwargs)

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

class Comment(Base):
    description = models.TextField(max_length=1200)
    rate = models.IntegerField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='user_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='film_comments')


def create_comment(sender, instance, **kwargs):

    c = Comment.objects.get(pk=instance.id)
    f = Film.objects.get(pk=c.film.id)
    f.rental_rate = Comment.objects.filter(film_id=c.film.id).aggregate(Avg('rate'))['rate__avg']
    f.save()


post_save.connect(create_comment, sender=Comment)
