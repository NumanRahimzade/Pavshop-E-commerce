from ast import Delete
from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT
)

from django.http import Http404

from product.api.serializers import ProductReadSerializer, ProductCreateSerializer
from product.models import ProductVersion


class ProductAPI(APIView):

    def get(self, request, *args, **kwargs):
        products = ProductVersion.objects.all().order_by('-created_at')
        serializer = ProductReadSerializer(products, many=True, context={'request': request})
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)


class ProductdetailApi(APIView):

    def get(self, request, *args, **kwargs):
        product = ProductVersion.objects.filter(id = kwargs['pk']).first()
        if product:
            serializer = ProductReadSerializer(product, context={'request': request})
            return Response(data=serializer.data)
        raise Http404


    def put(self, request, *args, **kwargs):
        product = ProductVersion.objects.filter(id = kwargs['pk']).first()
        if product:
            serializer = ProductCreateSerializer(data=request.data, instance=product)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)
        raise Http404


    def patch(self, request, *args, **kwargs):
        product = ProductVersion.objects.filter(id = kwargs['pk']).first()
        if product:
            serializer = ProductCreateSerializer(data=request.data, partial=True, instance=product)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)
        raise Http404


    def delete(self, request, *args, **kwargs):
        deleted_product, _ = ProductVersion.objects.filter(id = kwargs['pk']).delete()
        if deleted_product == 0:
            raise Http404
        return Response(data={}, status=HTTP_204_NO_CONTENT)

