from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_panel_view, name='home_panel'),
    
    path('products/', include('products.urls'), name='panel_products'),

    path('categorys/', include('products.urls'), name='panel_categorys'),
    
    path('sales/', orders_panel_view, name='panel_sales'),
    path('sale/<int:pk>/', order_panel_view, name='panel_sale'),
    path('add/sale/', create_order_panel_view, name='panel_create_sale'),
    path('edit/sale/', create_order_panel_view, name='panel_create_sale'),
    path('del/sale/<int:pk>/', delete_order_panel_view, name='panel_delete_sale'),


    # path('panel/delete/<int:pk>', products_panel_view, name='delete'),

]