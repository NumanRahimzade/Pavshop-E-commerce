from django.urls import path
from product.api.views import ProductListCreateAPI, ProductRetrieveUpdateDestroyAPIView, ImageListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPI.as_view(),),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),),
    path('products/images/', ImageListCreateAPIView.as_view(),),
]