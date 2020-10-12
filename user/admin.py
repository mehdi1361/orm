from django.contrib import admin
from user.models import Address, Phone


@admin.register(Address)
class AdderessAdmin(admin.ModelAdmin):
    list_display = ('address', 'district', 'postal_code')
    list_filter = ('address', )

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_active', 'phone_type')
    list_filter = ('phone_type', )
