from django.contrib import admin

from order.models import Order, Basket, BasketItem


admin.site.register([Order, Basket, BasketItem])