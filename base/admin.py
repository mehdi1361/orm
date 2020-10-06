from django.contrib import admin
from .models import Category, Language


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update')
    list_filter = ('last_update', )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update')
    list_filter = ('last_update', )
