from django.db import models
from base.models import Base, Language
import tsvector_field
from datetime import datetime

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
        if self.last_update is None:
            self.last_update = datetime.now()

    class Meta:
        db_table = 'movie_film'
        ordering = ['last_update']

    def __str__(self):
        return self.title

