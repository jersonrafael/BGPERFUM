from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products ,name='products'),
    path('product/<int:pk>/', filter_product ,name='product'),
    path('products/<int:pk>/', category_products ,name='category_products'),
    
    path('category/<int:pk>/', category_view ,name='category'),

    path('search/', search_product ,name='search'),
]
