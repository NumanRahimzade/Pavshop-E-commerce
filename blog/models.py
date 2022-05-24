from core.models import AbstractModel, Tag
from django.utils.translation import gettext_lazy as _
from product.models import Category
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy




User = get_user_model()


class Blog(AbstractModel):
    category=models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, related_name='blog', default='', on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True,related_name='blog_tags')
    title = models.CharField('Title', max_length=50, db_index=True)
    slug = models.SlugField(max_length=70, editable=False, blank=True, db_index=True)
    description = models.TextField('Description')
    image = models.ImageField(upload_to='blog_images/')


    def get_absolute_url(self):
        return reverse_lazy('blog_detail', kwargs={
            'slug': self.slug
        })


    def __str__(self):
        return self.title


# def story_object_creation(sender, **kwargs):
class Comment(AbstractModel):
    user=models.ForeignKey(User, related_name='commentuser',on_delete=models.CASCADE, default=1)
    blog=models.ForeignKey(Blog,related_name='blogcomment', on_delete=models.CASCADE)

    name=models.CharField('Name', max_length=50)
    email=models.EmailField('Email Address',max_length=50)
    subject = models.CharField('subject', max_length=80, db_index=True)
    review=models.TextField('Comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse_lazy('blog_detail', kwargs={
            'slug': self.blog.slug
        })



    

