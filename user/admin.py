from django.contrib import admin
from user.models import Address

@admin.register(Address)
class AdderessAdmin(admin.ModelAdmin):
    list_display = ('address', 'district', 'postal_code')
    list_filter = ('address', )
