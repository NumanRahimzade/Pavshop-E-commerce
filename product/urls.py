from django.urls import path
from product.views import productdetail, productlist


urlpatterns = [
    path('productdetail/',productdetail,name="productdetail"),
    path('productlist/',productlist,name="productlist"),

]