from django.db import models
from base.models import Base, City
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
