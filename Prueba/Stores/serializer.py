from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id','brand','identifier','name','address')

class BrandSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = ('id','name','logo')

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ('id','name','store','image','price')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','first_name')