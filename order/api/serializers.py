from ast import dump
from tkinter import FLAT
from urllib import request
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_serializer_method
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from order.models import BasketItem, Basket
from account.api.serializers import *
from product.api.serializers import *


User = get_user_model()


class BasketReadItemSerializer(serializers.ModelSerializer):
    productVersion = ProductReadSerializer()
    basket = serializers.SerializerMethodField()

    class Meta:
        model = BasketItem
        fields = (
            'id',
            'basket',
            'productVersion',
            'price',
            'sub_total',
            'count',
        )

    def get_basket(self, obj):
        return BasketSerializer(obj.basket).data


class BasketCreateItemSerializer(serializers.ModelSerializer):
    productVersion = str(ProductReadSerializer())
    # basket = str(BasketSerializer())
    
    class Meta:
        model = BasketItem
        fields = (
            'id',
            'productVersion',
            'price',
            'sub_total',
            'count',
        )

    def validate(self, data):
        context = self.context
        user = context['request'].user
        basket = user.basket
        print(basket)
        if not basket:
            basket = Basket.objects.create(author=user)
        data['basket'] = basket
        return super().validate(data)


class BasketSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    basketitem = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = (
            'author',
            'basketitem',
            'status',
        )

    @swagger_serializer_method(BasketReadItemSerializer(many=True))
    def get_basketitem(self, obj):
        items = obj.basketitems.all().values_list('id', "productVersion", 'price', 'sub_total', 'count')
        item_list = []
        for item in items:
            item_list.append(
                {
                    'id': item[0],
                    'productVersion':item[1],
                    'price':item[2],
                    'sub_total':item[3],
                    'count':item[4],
                }
            )
        return item_list