from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from order.models import BasketItem, Basket
from account.api.serializers import *
from product.api.serializers import *



class BasketSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    basketitem = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = (
            'author',
            'basketitem',
            'sub_total',
        )


    def get_basketitem(self, obj):
        items = obj.basketitems.all().values_list("productVersion", 'price', 'sub_total', 'count')
        item_list = []
        for item in items:
            item_list.append(
                {
                    'productVersion':item[0],
                    'price':item[1],
                    'sub_total':item[2],
                    'count':item[3],
                }
            )
        return item_list


class BasketItemSerializer(serializers.ModelSerializer):
    productVersion = ProductReadSerializer()
    basket = BasketSerializer()

    class Meta:
        model = BasketItem
        fields = (
            'basket',
            'productVersion',
            'price',
            'sub_total',
            'count',
        )