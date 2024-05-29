from django.urls import path
from .views import *


urlpatterns = [
    path('', products_panel_view, name='panel_products'),
    path('<int:pk>/', product_panel_view, name='panel_product'),
    path('add/product/', create_product_view, name='panel_create_product'),
    path('edit/<int:pk>/', modify_product_view, name='panel_modify_product'),
    path('del/product/<int:pk>/', delete_product_view, name='panel_delete_product'),

    path('', categorys_panel_view, name='panel_categorys'),
    path('category/<int:pk>/', category_panel_view, name='panel_category'),
    path('add/category/', create_category_view, name='panel_create_category'),
    path('edit/category/<int:pk>/', edit_category_view, name='panel_category'),
    path('del/category/<int:pk>/', delete_category_panel_view, name='delete_panel_category'),
]