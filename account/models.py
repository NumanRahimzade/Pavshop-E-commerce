from xxlimited import Null
from django.db import models
from django_countries.fields import CountryField    #country ucun
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField('image', upload_to='profile_images', null=True, blank=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    country = CountryField()    #country ucun
    town_city = models.CharField(max_length=50) 