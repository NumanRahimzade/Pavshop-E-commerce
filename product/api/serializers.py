from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from product.models import Product, ProductImages, ProductVersion, Category, Brand, Discount, PropertyValues, PropertyName, ProductImages
from core.models import Tag, Subscription


class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id', 
            'subcategory',
            'name',
        )


    def get_subcategory(self, obj):
        return obj.subcategory.name if obj.subcategory else "None"


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


class ProductCreateSerializer(serializers.ModelSerializer):
    
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
            'created_at',
            'updated_at',
        )


class ProductReadSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
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
        )

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


class ImageCreateSerializer(serializers.ModelSerializer):
    
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


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'email',
        )