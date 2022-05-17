from django.urls import path
from product.api.views import ProductAPI, ProductdetailApi

urlpatterns = [
    path('products/', ProductAPI.as_view(),),
    path('products/<int:pk>/', ProductdetailApi.as_view(),),
]