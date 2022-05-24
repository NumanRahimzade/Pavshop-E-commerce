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