from django.urls import path
from product.views import productdetail, ProductListView


urlpatterns = [
    # path('productdetail/',productdetail,name="productdetail"),
    path('productlist/',ProductListView.as_view(),name="productlist"),
    path('productdetail/<int:id>/',productdetail,name='productdetail')

]