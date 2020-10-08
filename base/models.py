from django.db import models
import datetime
import tsvector_field
class Base(models.Model):
    created_date = models.DateTimeField(verbose_name='created date', auto_now_add=True, null=True)
    updated_date = models.DateTimeField(verbose_name='created date', auto_now=True, null=True)

    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        ordering = ['last_update']

    def __str__(self):
        return self.name

class Language(Base):
    name = models.CharField(max_length=50)
    last_update = models.DateField()

    class Meta:
        ordering = ['last_update']

    def __str__(self):
        return self.name

class Country(Base):
    country = models.CharField(max_length=100)
    last_update = models.DateField()

    def __str__(self):
        return self.country

    class Meta:
        ordering = ['last_update']

class City(Base):
    city = models.CharField(max_length=50)
    last_update = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    class Meta:
        ordering = ['last_update']

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
    last_update = models.DateField(default=datetime.date.today())
    special_features = models.TextField()
    fulltext = tsvector_field.SearchVectorField()
    cover = models.ImageField(upload_to='media/cover', null=True)

    def save(self, *args, **kwargs):
        self.last_update = datetime.date.now()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'movie_film'
        ordering = ['last_update']

    def __str__(self):
        return self.title
