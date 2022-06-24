from django.urls import path
from product.api.views import (
    ProductListCreateAPI, ProductRetrieveUpdateDestroyAPIView, 
    ImageListCreateAPIView, SubscriptionView,CategoryView, 
    CategoryRetrieveUpdateDestroyAPIView, ReviewListCreateAPIView, )
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('products/', ProductListCreateAPI.as_view(),),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),),
    path('products/images/', ImageListCreateAPIView.as_view(),),
    path('products/reviews/', ReviewListCreateAPIView.as_view(),),
    path('subscriptions/', SubscriptionView.as_view(), ),
    path('categories/', CategoryView.as_view(),),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(),),
]



urlpatterns = format_suffix_patterns(urlpatterns)
