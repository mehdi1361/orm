from django.contrib import admin
from movie.models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_year', 'language', 'last_update')
    list_filter = ('last_update', )
