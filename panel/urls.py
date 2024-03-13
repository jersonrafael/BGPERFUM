from django.urls import path
from .views import *

urlpatterns = [
    path('', home_panel_view, name='home_panel'),
    
    path('products/', products_panel_view, name='panel_products'),
    path('product/<int:pk>/', product_panel_view, name='panel_product'),
    path('add/product/', create_product_view, name='panel_create_product'),
    path('edit/<int:pk>/', modify_product_view, name='modify'),
    path('del/product/<int:pk>/', delete_product_view, name='panel_delete_product'),

    path('categorys/', categorys_panel_view, name='panel_categorys'),
    path('add/category/', create_category_view, name='panel_create_category'),
    
    path('sales/', products_panel_view, name='panel_sales'),

    # path('panel/delete/<int:pk>', products_panel_view, name='delete'),

]