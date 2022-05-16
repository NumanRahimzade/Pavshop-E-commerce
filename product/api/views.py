from rest_framework.views import APIView
from rest_framework.response import Response

from product.api.serializers import ProductReadSerializer, ProductCreateSerializer
from product.models import ProductVersion


class ProductAPI(APIView):

    def get(self, request, *args, **kwargs):
        stories = ProductVersion.objects.all().order_by('-created_at')
        serializer = ProductReadSerializer(stories, many=True, context={'request': request})
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)