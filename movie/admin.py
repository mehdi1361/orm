from django.contrib import admin
from movie.models import Film, Actor

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_year', 'language', 'last_update')
    list_filter = ('last_update', )

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    list_filter = ('last_update', )
