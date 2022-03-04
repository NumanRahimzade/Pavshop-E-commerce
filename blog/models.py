from core.models import AbstractModel
from django.db import models


class Blog(AbstractModel):

    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.title