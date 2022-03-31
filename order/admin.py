from django.contrib import admin

from order.models import Order, Basket, BasketItem,BillingDetail


admin.site.register([Order, Basket, BasketItem,BillingDetail])