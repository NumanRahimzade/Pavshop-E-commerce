from django.contrib import admin

from product.models import Order, Basket, BasketItem


admin.site.register([Order, Basket, BasketItem])
