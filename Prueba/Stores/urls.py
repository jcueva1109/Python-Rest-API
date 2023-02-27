from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.getStores),
    path('post/',views.getStores),
]