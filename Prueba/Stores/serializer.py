from rest_framework import serializers
from .models import *

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id','brand','identifier','name','address')

class BrandSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = ('id','name','logo')