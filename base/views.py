from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, response
from .models import Product
from .serializers import ProductSerializer
# from .products import products

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [

    ]
    return Response('hello')


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer =  ProductSerializer(products, many = True)
    return Response(serializer.data)



@api_view(['GET'])
def getProduct(request, pk):
   product = Product.objects.get(_id=pk)
   serializer = ProductSerializer(product, many=False)
   return Response(serializer.data)

 



