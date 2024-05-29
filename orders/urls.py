from django.urls import path, include
from .views import *


urlpatterns = [
    path('', orders_panel_view, name='panel_sales'),
    path('sale/<int:pk>/', order_panel_view, name='panel_sale'),
    path('add/sale/', create_order_panel_view, name='panel_create_sale'),
    path('edit/sale/', create_order_panel_view, name='panel_create_sale'),
    path('del/sale/<int:pk>/', delete_order_panel_view, name='panel_delete_sale'),
]