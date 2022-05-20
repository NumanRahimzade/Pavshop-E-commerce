from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from product.models import Product, ProductVersion, Category, Brand, Discount, PropertyValues, PropertyName
from core.models import Tag


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
    product = ProductSerializer()
    discount = DiscountSerializer()
    property = PropertyValuesSerializer(many=True)
    tags = TagSerializer(many=True)
    # category = CategorySerializer()
    
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

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
        )