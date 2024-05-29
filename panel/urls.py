from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_panel_view, name='home_panel'),
    
    path('products/', include('products.urls'), name='panel_products'),

    path('categorys/', include('products.urls'), name='panel_categorys'),
    
    path('sales/', include('orders.urls'), name='panel_sales'),
]