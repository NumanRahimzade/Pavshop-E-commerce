from core.models import AbstractModel
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Blog(AbstractModel):
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)

    
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.title