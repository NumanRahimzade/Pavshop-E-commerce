from ast import Delete
from functools import partial
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT
)

from django.http import Http404

from product.api.serializers import ProductReadSerializer, ProductCreateSerializer, ImageCreateSerializer, SubscriptionSerializer
from product.models import ProductImages, ProductVersion
from core.models import Subscription

###### API with APIView inherit #######
# class ProductAPI(APIView):

#     def get(self, request, *args, **kwargs):
#         products = ProductVersion.objects.all().order_by('-created_at')
#         category = request.GET.get('category') # ?category=2
#         tags = request.GET.get('tags') # ?category=2
        
#         if category:
#             products = products.filter(product__category__id=category) # filtered products
#         if tags:
#             products = products.filter(tags__id=tags) # filtered products
#         serializer = ProductReadSerializer(products, many=True, context={'request': request})
#         return Response(data=serializer.data)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = ProductCreateSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=HTTP_201_CREATED)


# class ProductDetailApi(APIView):

#     def get(self, request, *args, **kwargs):
#         product = ProductVersion.objects.filter(id = kwargs['pk']).first()
#         if product:
#             serializer = ProductReadSerializer(product, context={'request': request})
#             return Response(data=serializer.data)
#         raise Http404


#     def put(self, request, *args, **kwargs):
#         product = ProductVersion.objects.filter(id = kwargs['pk']).first()
#         if product:
#             serializer = ProductCreateSerializer(data=request.data, instance=product)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(data=serializer.data, status=HTTP_200_OK)
#         raise Http404


#     def patch(self, request, *args, **kwargs):
#         product = ProductVersion.objects.filter(id = kwargs['pk']).first()
#         if product:
#             serializer = ProductCreateSerializer(data=request.data, partial=True, instance=product)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(data=serializer.data, status=HTTP_200_OK)
#         raise Http404


#     def delete(self, request, *args, **kwargs):
#         deleted_product, _ = ProductVersion.objects.filter(id = kwargs['pk']).delete()
#         if deleted_product == 0:
#             raise Http404
#         return Response(data={}, status=HTTP_204_NO_CONTENT)

######  API with APIView inherit #######




##### API with generics #####
class CustomListCreateAPIView(ListCreateAPIView):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.request.method)


class ProductListCreateAPI(CustomListCreateAPIView, django_filters.FilterSet):
    queryset = ProductVersion.objects.all().order_by('-created_at')
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,  filters.OrderingFilter)
    filter_fields = ('product__category__id', 'tags')
    serializer_classes = {
        'GET': ProductReadSerializer,
        'POST': ProductCreateSerializer
    }


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductCreateSerializer


class ImageListCreateAPIView(ListCreateAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ImageCreateSerializer
##### API with generics #####

class SubscriptionView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response

from product.api.serializers import CategoryReadSerializer,CategoryCreateSerializer
from product.models import Category
from django.http import Http404
from rest_framework import status



class CategoryAPI(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategoryReadSerializer(categories, many=True, context={'request': request} )
        return Response(data=serializer.data)


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CategoryCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    




class CategoryDetailAPI(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categories = self.get_object(pk)
        serializer = CategoryReadSerializer(categories)
        return Response(serializer.data)

    def put(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategoryCreateSerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categories = self.get_object(pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
