from django.db import models
from base.models import Base, City
from user.validator import phone_validator
from django.contrib.auth.models import User

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
        ("MOBILE", "mobile"),
        ("PHONE", "phone"),
    ]

    phone_number = models.CharField(max_length=50, validators=[phone_validator, ])
    is_active = models.BooleanField()
    phone_type = models.CharField(max_length=150, choices=PHONE_TYPE_CHOICE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.phone_number[:3] in ["090", "091", "092", "093"]:
            Phone.phone_number = "PHONE"

        else:

            Phone.phone_number = "phone"
        super(Phone, self).save(*args, **kwargs)
