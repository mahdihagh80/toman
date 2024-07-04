from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import ProductImage, Product
from .serializers import ImageUploaderSerializer, ProductCreationSerializer, ProductSerializer


class ImageUploadView(CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = ImageUploaderSerializer
    queryset = ProductImage.objects.all()

class ImageDeleteRetrieveView(DestroyAPIView, RetrieveAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = ImageUploaderSerializer
    queryset = ProductImage.objects.all()



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()


    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreationSerializer
        return ProductSerializer

# class ProductCreationView(CreateAPIView):
#     serializer_class = ProductCreationSerializer
#     queryset = Product.objects.all()
#
# class ProductDeleteRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
