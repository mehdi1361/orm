from django.contrib import admin
from .models import Category, Language, Country, City, Template


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update')
    list_filter = ('last_update', )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update')
    list_filter = ('last_update', )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country', 'last_update')
    list_filter = ('last_update', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'last_update')
    list_filter = ('last_update', )


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('template',)
    list_filter = ('template',)
