from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from core.models import Tag
from django.template.defaultfilters import slugify
# from account.utils import image_resize

User = get_user_model()

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Category(AbstractModel):
    subcategory=models.ForeignKey('self',related_name='categories', default='', on_delete=models.CASCADE, null=True, blank=True)

    name=models.CharField('Name',max_length=70)
    

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        count = 0
        for i in self.products.all():
            count += i.productversions.count()
        return count
        return self.products.count()

    @property
    def blog_count(self):
        return self.blogs.count()

class Brand(AbstractModel):
    name=models.CharField('Name',max_length=70)

    def __str__(self):
        return self.name


class Product(AbstractModel):
    brand=models.ForeignKey('Brand',related_name='productbrand',default="", on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name='products',default="", on_delete=models.CASCADE)
    title=models.CharField('Title', max_length=50)
    
    
    def __str__(self):
            return self.title

    @property
    def main_version(self):
        return self.productversions.first()


class PropertyName(AbstractModel):
    category=models.ForeignKey(Category,related_name='propertynames',default="", on_delete=models.SET_NULL, null=True, blank=True)

    name=models.CharField('Name',max_length=70)


    class Meta:
        verbose_name = 'Property Name'
        verbose_name_plural = 'Property Names'

    def __str__(self):
        return self.name

    
    @property
    def main_values(self):
        return self.propertyvalues.first()


class PropertyValues(AbstractModel):
    propertyname=models.ForeignKey(PropertyName, related_name='propertyvalues',default="", on_delete=models.CASCADE, verbose_name="Property Name")

    value=models.CharField('Value',max_length=100)

    class Meta:
        verbose_name = 'Property Value'
        verbose_name_plural = 'Property Values'

    def __str__(self):
        return self.value


class ProductVersion(AbstractModel):
    product=models.ForeignKey(Product, related_name='productversions',default="", on_delete=models.CASCADE)
    discount=models.ForeignKey('Discount',related_name='productdiscount',default="", on_delete=models.CASCADE, blank=True, null=True)
    property=models.ManyToManyField(PropertyValues,blank=True)

    title=models.CharField('Title', max_length=50)
    slug = models.SlugField(max_length=70, editable=False, blank=True, db_index=True) 
    code=models.CharField('Code',max_length=50)
    price=models.CharField('Price',max_length=40)
    discount_price=models.CharField('DiscountPrice',max_length=40, null=True, blank=True)
    stock=models.IntegerField('Stock')
    tags=models.ManyToManyField(Tag,blank=True,related_name='product_tags')
    


    def __str__(self):
        return self.title


    def main_image(self):
        return self.productimage.all().order_by('is_main').first()

    
    def review_count(self):
        return self.reviews.count()

    def get_absolute_url(self):
        return reverse_lazy('productdetail', kwargs={
            'pk': self.id
        })


class ProductImages(AbstractModel):
    version=models.ForeignKey(ProductVersion,related_name='productimage',default="", on_delete=models.CASCADE)

    image = models.ImageField(upload_to='product_images/')
    cover_image = models.ImageField('cover image', upload_to='product_images/', null=True, blank=True)
    is_main=models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


    # def save(self, commit=True, *args, **kwargs):
    #     if commit:
    #         image_resize(self.image, 800, 1010)
    #         super().save(*args, **kwargs)


class Discount(AbstractModel):
    title=models.CharField('Title', max_length=80)
    percentage=models.CharField('Percentage', max_length=20, null=True, blank=True)
    value=models.IntegerField('Value', null=True, blank=True)

    def __str__(self):
        return self.title
        

class WishList(AbstractModel):
    productversion=models.ManyToManyField(ProductVersion, related_name='wishproduct',blank=True)
    user=models.OneToOneField(User,default="",on_delete=models.CASCADE)


class Review(AbstractModel):
    CHOICES = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )
    user=models.ForeignKey(User, related_name='reviewuser',on_delete=models.CASCADE)
    productversion=models.ForeignKey(ProductVersion,related_name='reviews', on_delete=models.CASCADE)
    comment=models.CharField('Comment', max_length=300, blank=True, null=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(choices=CHOICES, verbose_name="Rating", default=1)

    def __str__(self):
        return self.productversion.title
    

    def get_absolute_url(self):
        return reverse_lazy('productdetail', kwargs={
            'pk': self.productversion.id
        })