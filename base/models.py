from django.db import models

class Base(models.Model):
    created_date = models.DateTimeField(verbose_name='created date', auto_now_add=True, null=True)
    updated_date = models.DateTimeField(verbose_name='created date', auto_now=True, null=True)

    class Meta:
        abstract = True

class LocalConf(models.Model):
    fa_name = models.CharField(max_length=50, null=True)

    class Meta:
        abstract = True


class Category(Base, LocalConf):
    name = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        ordering = ['last_update']

    def __str__(self):
        return self.name

class Language(Base, LocalConf):
    name = models.CharField(max_length=50)
    last_update = models.DateField()

    class Meta:
        ordering = ['last_update']

    def __str__(self):
        return self.name

class Country(Base, LocalConf):
    country = models.CharField(max_length=100)
    last_update = models.DateField()

    def __str__(self):
        return self.country

    class Meta:
        ordering = ['last_update']

class City(Base, LocalConf):
    city = models.CharField(max_length=50)
    last_update = models.DateField()
    country = models.ForeignKey(Country,related_name='cities' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    class Meta:
        ordering = ['last_update']


class Template(Base):
    template = models.CharField(max_length=1500)

    def __str__(self):
        return self.template
