#from django.http import response
#from admin.products2.models import Product
#from django.shortcuts import render

from rest_framework import viewsets, status
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
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        
    def destroy(self, reuqest, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)

#class UserAPIView(UserAPIView)
        