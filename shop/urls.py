from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products ,name='products'),
    path('products/<int:pk>', category_products ,name='category_products'),
]