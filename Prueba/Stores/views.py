from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *

# Create your views here.
@api_view(['GET'])
def getStores(request):
    store = Store.objects.all()
    serializer = StoreSerializer(store, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getBrands(request):
    brand = Brand.objects.all()
    serializer = BrandSerializer(brand, many=True)
    return Response(serializer.data)