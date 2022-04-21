from django.urls import path
from product.views import productdetail, productlist, ProductDetailView



urlpatterns = [
    path('productdetail/<int:pk>/',ProductDetailView.as_view(),name="productdetail"),
    # path('productdetail/<int:id>/',productdetail,name="productdetail"),
    path('productlist/',productlist,name="productlist"),

]