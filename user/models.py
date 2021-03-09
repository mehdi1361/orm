from django.db import models
from base.models import Base, City, Template
from user.validator import phone_validator
from django.contrib.auth.models import User
from movie.models import Film


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
    template = models.ManyToManyField(Template, through='Sms')

    def save(self, *args, **kwargs):
        if self.phone_number[:3] in ["090", "091", "092", "093"]:
            Phone.phone_number = "PHONE"

        else:

            Phone.phone_number = "phone"


class Cart(Base):
    sequence_name = models.CharField(max_length=100)
    film = models.ManyToManyField(Film, through="CartFilm")


class CartFilm(Base):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "movie_cart_film"
        ordering = ["quantity"]

    def __str__(self):
        return self.quantity


class Sms(Base):
    state_choices = [
        ("DRAFT", "draft"),
        ("SEND", "send"),
    ]
    message = models.CharField(max_length=150, choices=state_choices)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)


class Verification(Base):
    verification = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.CharField(max_length=150)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        Verification.objects.filter(user=self.user, device=self.device).update(active=False)
        super(Verification, self).save(*args, **kwargs)

    @classmethod
    def verify_test(cls, **kwargs):
        u = User.objects.get(username=kwargs['dev_id'])
        v = Verification.objects.get(user=u, verification=kwargs["verify_code"], active=True)

        if v:
            v.active = False
            v.save()
            return True

        else:
            return False
