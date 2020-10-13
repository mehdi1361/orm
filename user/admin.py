from django.contrib import admin
from user.models import Address, Phone, CartFilm, Sms


@admin.register(Address)
class AdderessAdmin(admin.ModelAdmin):
    list_display = ('address', 'district', 'postal_code')
    list_filter = ('address', )

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_active', 'phone_type')
    list_filter = ('phone_type', )

@admin.register(CartFilm)
class CartFilmAdmin(admin.ModelAdmin):
    list_display = ('film', 'cart', 'quantity')
    list_filter = ('quantity', )

@admin.register(Sms)
class SmsAdmin(admin.ModelAdmin):
    list_display = ("message",)
    list_filter = ("message",)
