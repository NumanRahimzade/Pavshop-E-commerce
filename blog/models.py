from unicodedata import category
from core.models import AbstractModel
from django.db import models
from django.contrib.auth import get_user_model
from product.models import Category



User = get_user_model()


class Tag(AbstractModel):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Blog(AbstractModel):
    category=models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True,related_name='blog_tags')

    
    title = models.CharField('Title', max_length=50, db_index=True)
    description = models.TextField('Description')
    image = models.ImageField(upload_to='media/blog_images/')

    def __str__(self):
        return self.title


class Comment(AbstractModel):
    user=models.ForeignKey(User, related_name='commentuser',on_delete=models.CASCADE, default=1)
    blog=models.ForeignKey(Blog,related_name='blogcomment', on_delete=models.CASCADE)


    review=models.CharField('Comment', max_length=300)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.blog.title




    

