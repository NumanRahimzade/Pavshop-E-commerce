from xxlimited import Null
from PIL import Image
from django.db import models
from django_countries.fields import CountryField    #country ucun
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from .utils import image_resize


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField('image', upload_to='profile_images/', null=True, blank=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    country = CountryField()    #country ucun
    town_city = models.CharField(max_length=50)

   #### resize user image
    # def save(self, commit=True, *args, **kwargs):
    #     if commit:
    #         image_resize(self.image, 185, 185)
    #         super().save(*args, **kwargs)

    #### end resize user image      
