from django.contrib import admin
from movie.models import Film, Actor, Comment


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_year', 'language', 'last_update')
    list_filter = ('last_update', )

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('last_update', )

@admin.register(Comment)
class Actorcomment(admin.ModelAdmin):
    list_display = ('rate', 'description')
    list_filter = ('rate', 'description')
