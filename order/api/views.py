from urllib import request
from rest_framework.response import Response
from order.api.serializers import BasketSerializer, BasketReadItemSerializer, BasketCreateItemSerializer
from django.contrib.auth import get_user_model
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# import django_filters.rest_framework
# from rest_framework import filters
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from django.http import Http404
from order.models import *


User = get_user_model()


class CustomListCreateAPIView(ListCreateAPIView):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.request.method)


class BasketViewAPI(ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketItemViewAPI(CustomListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = BasketItem.objects.all()
    serializer_classes = {
        'POST': BasketCreateItemSerializer,
        'GET': BasketReadItemSerializer
    }


    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(basket__author=user).exclude(basket__status = True).order_by('-created_at')


class BasketItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = BasketItem.objects.all()
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasketReadItemSerializer
        else:
            return BasketCreateItemSerializer



