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

from product.api.serializers import ProductReadSerializer, ProductCreateSerializer
from product.models import ProductVersion

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


##### API with generics #####