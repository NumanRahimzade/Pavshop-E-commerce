from django.db import models

class AbstractModel(models.Model):


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):
    
    full_name = models.CharField('Full Name', max_length=50)
    email = models.EmailField('Email', max_length=40)
    phone = models.CharField('Phone', max_length=20)
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('Message', help_text='Buraya mesajinizi daxil edin!')

    def __str__(self):
        return self.full_name


class NewsLatest(AbstractModel):
    
    title = models.CharField('TITLE', max_length=50)
    description = models.TextField('DESCRIPTION', )

    def __str__(self):
        return self.title


class Subscription(AbstractModel):

    # newslatest = models.ManyToManyField(NewsLatest, blank=True, related_name='news')
    
    email = models.EmailField('EMAIL', max_length=40)

    def __str__(self):
        return self.email








