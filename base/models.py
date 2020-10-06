from django.db import models


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
