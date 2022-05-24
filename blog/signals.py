import datetime
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from blog.models import Blog
from slugify import slugify



# @receiver(pre_save, sender=Blog)
# def blog_object_creation(sender, instance, **kwargs):
#     print(instance.pk)
#     instance.slug = f"{slugify(instance.title)}-{instance.id}"
#     # instance.save()
#     instance.slug = f"{slugify(instance.title)}-{instance.id}"
#     instance.save()

@receiver(post_save, sender=Blog)
def story_object_creation(sender, instance, created, **kwargs):
    
    old_slug = instance.slug
    new_slug = f"{slugify(instance.title)}-{instance.id}"  #id version
    # new_slug = f"{slugify(instance.title+datetime.datetime.now())}-{instance.id}"  ### id with datetime
    if old_slug != new_slug:
        instance.slug = new_slug
        instance.save()
        

# @receiver(pre_save, sender=Recipe)
# def story_object_creation(sender, **kwargs):