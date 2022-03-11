from django.urls import path
from order.views import checkout, shoppingcart


urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('shoppingcart/',shoppingcart,name="shoppingcart"),

]


