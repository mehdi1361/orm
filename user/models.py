from django.db import models
from base.models import Base, City
from django.contrib.auth.models import User
from user.validator import phone_validator

class Address(Base):
    address = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    class Meta:
        db_table = "user_address"
        ordering = ["address"]

    def __str__(self):
        return self.address


class Phone(Base):

    PHONE_TYPE_CHOICE = [
        ("phone", "mobile")
    ]

    phone_number = models.CharField(max_length=50, validators=[phone_validator])
    is_active = models.BooleanField()
    phone_type = models.CharField(max_length=150, choices=PHONE_TYPE_CHOICE)

    def save(self, *args, **kwargs):
        if self.phone_number.startswith("092"):
            Phone.phone_number = "phone"
            super(Phone, self).save(*args, **kwargs)

        elif self.phone_number.startswith("091"):
            Phone.phone_number = "phone"
            super(Phone, self).save(*args, **kwargs)

        elif self.phone_number.startswith("090"):
            Phone.phone_number = "phone"
            super(Phone, self).save(*args, **kwargs)

        elif self.phone_number.startswith("093"):
            Phone.phone_number = "phone"
            super(Phone, self).save(*args, **kwargs)
        else:
            raise ("the not phone number format")

class Cart(Base):
    sequence_name = models.CharField(max_length=100)
