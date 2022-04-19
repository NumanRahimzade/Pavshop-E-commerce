from django.urls import path
from product.views import productlist, PrdoductDetailView


urlpatterns = [
    path('productdetail/<int:pk>/',PrdoductDetailView.as_view(),name="productdetail"),
    path('productlist/',productlist,name="productlist"),

]