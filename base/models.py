from django.db import models
class Base(models.Model):
    created_date = models.DateField(verbose_name='created date', auto_now_add=True)
    updated_date = models.DateField(verbose_name='updated date', auto_now=True)

    class Meta:
        abstract = True
