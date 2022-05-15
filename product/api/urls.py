from django.urls import path
from product.api.views import ProductAPI

urlpatterns = [
    path('products/', ProductAPI.as_view(),),
]