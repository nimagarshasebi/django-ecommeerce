from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    phone_number=PhoneNumberField()
    def __str__(self):
        return f'{self.username} profile'

class Address(models.Model):
    customer = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    firstname_customer = models.CharField(max_length=100)
    lastname_customer = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    default_address=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer, self.state, self.county, self.city, self.street_address, self.postal_code}'

