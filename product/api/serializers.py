from rest_framework import serializers
from product.models import Category

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 
            'name',
        )



class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'subcategory',
        )




class CategoryReadSerializer(serializers.ModelSerializer):
    subcategory=SubcategorySerializer()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'subcategory',
        )

