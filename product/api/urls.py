from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from product.api.views import CategoryAPI, CategoryDetailAPI

urlpatterns = [
    path('categories/', CategoryAPI.as_view(),),
    path('categories/<int:pk>/', CategoryDetailAPI.as_view(),),
] 


urlpatterns = format_suffix_patterns(urlpatterns)