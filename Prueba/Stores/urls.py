from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('stores',views.getStores),
    path('brands',views.getBrands),
]