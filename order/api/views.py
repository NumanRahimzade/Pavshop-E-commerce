from order.api.serializers import BasketSerializer, BasketItemSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from django.http import Http404
from order.models import *


class BasketViewAPI(ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketItemViewAPI(ListCreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

