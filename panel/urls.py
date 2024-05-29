from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_panel_view, name='home_panel'),
    
    path('products/', include('products.urls')),

    path('categorys/', include('products.urls')),
    
    path('sales/', include('orders.urls')),
]