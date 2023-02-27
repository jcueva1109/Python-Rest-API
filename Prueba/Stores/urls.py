from django.urls import path, include
from . import views
from django.conf import settings
from oauth2_provider.views import TokenView

urlpatterns = [
    path('stores',views.getStores),
    path('brands',views.getBrands),
    path('deals',views.getDeals),
    path('auth',TokenView.as_view(), name='token'),
]