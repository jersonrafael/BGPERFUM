from django.urls import path
from .views import *


urlpatterns = [
    path('', products_panel_view, name='panel_products'),
    path('<int:pk>/', product_panel_view, name='panel_product'),
    path('add/product/', create_product_view, name='panel_create_product'),
    path('edit/<int:pk>/', modify_product_view, name='panel_modify_product'),
    path('del/product/<int:pk>/', delete_product_view, name='panel_delete_product'),
]