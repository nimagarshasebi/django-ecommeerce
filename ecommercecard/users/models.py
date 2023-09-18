from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    phone_number=PhoneNumberField()
    def __str__(self):
        return f'{self.username} profile'



