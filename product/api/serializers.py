
from audioop import reverse
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from product.models import Product, ProductImages, ProductVersion, Category, Brand, Discount, PropertyValues, PropertyName, ProductImages, Review
from core.models import Tag, Subscription
from account.api.serializers import *


User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField()
    subcategory_id = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id', 
            'name',
            'subcategory',
            'subcategory_id',
        )


    def get_subcategory(self, obj):
        return obj.subcategory.name if obj.subcategory else "None"

    
    def get_subcategory_id(self, obj):
        return obj.subcategory.id if obj.subcategory else "None"


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'subcategory',
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
        )


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            'id',
            'title',
            'percentage',
            'value',
        )


class PropertySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = PropertyName
        fields = (
            'id',
            'name',
            'category',
        )


class PropertyValuesSerializer(serializers.ModelSerializer):
    propertyname = PropertySerializer()
    
    class Meta:
        model = PropertyValues
        fields = (
            'id',
            'propertyname',
            'value',
        )
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    
    class Meta:
        model = Product
        fields = (
            'id', 
            'brand',
            'category',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title'
        )


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImages
        fields = (
            'version', ## productverion id
            'image',
            'cover_image',
            'is_main',
            'created_at',
            'updated_at',
            
        )


class ProductCreateSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    class Meta:
        model = ProductVersion
        fields = (
            'product',
            'discount',
            'property',
            'title',
            'slug',
            'code',
            'price',
            'stock',
            'tags',
            'image',
            'review',
            'created_at',
            'updated_at',
        )
    
    # def get_detail_url(self):
    #     return reverse_lazy


    @swagger_serializer_method(ImageSerializer(many=True))
    def get_image(self, obj):
        images = obj.productimage.all().values_list("image", 'cover_image')
        img_list = []
        for img in images:
            img_list.append(
                {
                    'image':img[0],
                    'cover_image':img[1]
                }
            )
        return img_list


    def get_review(self, obj):
        reviews = obj.reviews.all().values_list("comment", 'reply')
        reviews_list = []
        for i in reviews:
            reviews_list.append(
                {
                    'comment':i[0],
                    'reply':i[1]
                }
            )
        return reviews_list


class ProductReadSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()
    product = ProductSerializer()
    discount = DiscountSerializer()
    property = PropertyValuesSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = ProductVersion
        fields = (
            'id',
            'product',
            'discount',
            'property',
            'title',
            'slug',
            'code',
            'price',
            'stock',
            'tags',
            'created_at',
            'updated_at',
            'image',
            'review',
        )


    @swagger_serializer_method(ImageSerializer(many=True))
    def get_image(self, obj):
        images = obj.productimage.all().values_list("image", 'cover_image')
        img_list = []
        for img in images:
            img_list.append(
                {
                    'image':img[0],
                    'cover_image':img[1]
                }
            )
        return img_list


    def get_review(self, obj):
        reviews = obj.reviews.all().values_list("comment", 'reply')
        reviews_list = []
        for i in reviews:
            reviews_list.append(
                {
                    'comment':i[0],
                    'reply':i[1]
                }
            )
        return reviews_list


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'email',
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = str(UserSerializer())

    class Meta:
        model = Review
        fields = (
            'user',
            'productversion',
            'comment',
            'reply',
        )


# WISHLIST WISHLIST HAS TO BE CREATED