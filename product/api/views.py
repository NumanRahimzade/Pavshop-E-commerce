from ast import Delete
from functools import partial
from unicodedata import category
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)

from django.http import Http404
# from rest_framework.parsers import MultiPartParser, FormParser

from product.api.serializers import ( 
    ProductReadSerializer, ProductCreateSerializer, 
    ImageSerializer, SubscriptionSerializer,
    CategorySerializer,CategoryCreateSerializer, 
    ReviewSerializer,)
from product.models import ProductImages, ProductVersion, Category, Review
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
    serializer_class = ImageSerializer
    # parser_classes = (MultiPartParser, FormParser)


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SubscriptionView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorySerializer
        return CategoryCreateSerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorySerializer
        return CategoryCreateSerializer


##### API with generics #####

# class CategoryAPI(APIView):

#     def get(self, request, *args, **kwargs):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True, context={'request': request} )
#         return Response(data=serializer.data)


#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = CategoryCreateSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=HTTP_201_CREATED)

 
# class CategoryDetailAPI(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         categories = self.get_object(pk)
#         serializer = CategorySerializer(categories)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         categories = self.get_object(pk)
#         serializer = CategoryCreateSerializer(categories, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         categories = self.get_object(pk)
#         categories.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
