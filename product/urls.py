from django.urls import path
from product.views import productdetail, ProductListView, ProductDetailView, SearchView


urlpatterns = [
    # path('productdetail/',productdetail,name="productdetail"),
    path('productlist/',ProductListView.as_view(),name="productlist"),
    path('productdetail/<int:pk>/',ProductDetailView.as_view(),name='productdetail'),
    path('search/',SearchView.as_view(),name='search'),
]