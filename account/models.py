from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class User(AbstractUser):
    # USERNAME_FIELD = 'email'
    # email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    # REQUIRED_FIELDS = [] 
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile_images')
    phone_number=models.CharField('PHONE',max_length=30)
    address=models.CharField('ADDRESS',max_length=100)
    country=CountryField()
    city=models.CharField('TOWN/CITY',max_length=100)
  
