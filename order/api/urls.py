from django.urls import path
from order.api.views import (
     BasketViewAPI, BasketItemViewAPI
     )

urlpatterns = [
    path('baskets/', BasketViewAPI.as_view(), ),
    path('basketitems/', BasketItemViewAPI.as_view(), )
]