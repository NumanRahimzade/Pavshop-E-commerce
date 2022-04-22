from django.template import Library
from product.models import Category

register = Library()



@register.simple_tag
def get_categories(offset, limit):
    return Category.objects.all().order_by('created_at')[offset:limit]
    