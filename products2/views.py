#from django.http import response
#from admin.products2.models import Product
#from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response


from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        print("productViewset:LIST")
        print(serializer.data)
        print("END !")
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, reuqest, pk=None):
        pass