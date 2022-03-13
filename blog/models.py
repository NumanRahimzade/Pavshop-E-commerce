from turtle import title
from core.models import AbstractModel
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryBlog(AbstractModel):

    title = models.CharField('Title', max_length=30)

    def __str__(self):
        return self.title


class Tag(AbstractModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Blog(AbstractModel):
    category = models.ForeignKey(CategoryBlog, related_name='blogs', on_delete=models.CASCADE)
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    
    title = models.CharField('Title', max_length=50, db_index=True)
    description = models.TextField('Description')

    def __str__(self):
        return self.title