from django.template import Library
from product.models import Category
from core.models import Tag
from django.db import models

register = Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_popular_tags():
    return Tag.objects.annotate(num_tags=models.Count('blog_tags')).order_by('-num_tags')[:10]