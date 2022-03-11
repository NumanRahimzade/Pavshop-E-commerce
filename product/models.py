from pyexpat import model
from unicodedata import category
from django.db import models


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Category(AbstractModel):
    subcategory=models.ForeignKey('self',related_name='categories',on_delete=models.CASCADE)

    name=models.CharField('Name',max_length=70)
    

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(AbstractModel):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)


class PropertyName(AbstractModel):
    category=models.ForeignKey(Category,related_name='propertynames',on_delete=models.CASCADE)

    name=models.CharField('Name',max_length=70)


    class Meta:
        verbose_name = 'Property Name'
        verbose_name_plural = 'Propery Names'

    def __str__(self):
        return self.name


class PropertyValues(AbstractModel):
    value=models.CharField('Value',max_length=100)


    class Meta:
        verbose_name = 'Property Value'
        verbose_name_plural = 'Property Values'

    def __str__(self):
        return self.value


class ProductVersion(AbstractModel):
    product=models.ForeignKey(Product,)

    title=models.CharField('Title', max_length=50)
    code=models.CharField('Code',max_length=50)
    price=models.CharField('Price',max_length=40)
    stock=models.IntegerField('Stock')

    def __str__(self):
        return self.title


class Brand(AbstractModel):
    name=models.CharField('Name',max_length=70)

    def __str__(self):
        return self.name


class ProductImages(AbstractModel):
    image = models.ImageField(upload_to='media/product_images/')
    is_main=models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Discount(AbstractModel):
    title=models.CharField('Title', max_length=80)
    percentage=models.CharField('Percentage', max_length=20)
    value=models.IntegerField('Value')

    def __str__(self):
        return self.title
        





