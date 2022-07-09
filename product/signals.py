from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from product.models import ProductVersion
from slugify import slugify



# @receiver(pre_save, sender=ProductVersion)
# def product_object_creation(sender, instance, **kwargs):
    
#     instance.slug = f"{slugify(instance.title)}-{instance.id}"


@receiver(post_save, sender=ProductVersion)
def product_object_creation(sender, instance, created, **kwargs):
    print(created)
    old_slug = instance.slug
    new_slug = f"{slugify(instance.title)}-{instance.id}"
    if old_slug != new_slug:
        instance.slug = new_slug
        instance.save()
        print('isledi')


@receiver(pre_save, sender=ProductVersion)
def get_discount_price(sender, instance, **kwargs):
        
    if instance.discount:
        a = float(instance.price)*float(instance.discount.percentage)/100
        result = float(instance.price)-float(a)
        instance.discount_price =result
        
