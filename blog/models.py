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


class Comment(AbstractModel):
    user=models.ForeignKey(User, related_name='commentuser',on_delete=models.CASCADE, default=1)
    blog=models.ForeignKey(Blog,related_name='blogcomment', on_delete=models.CASCADE)


    review=models.CharField('Comment', max_length=300)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.blog.title