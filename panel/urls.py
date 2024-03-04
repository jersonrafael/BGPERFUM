from django.urls import path
from .views import *

urlpatterns = [
    path('panel', home_panel_view, name='home_panel'),
    path('panel/products', products_panel_view, name='panel_products'),
    path('panel/categorys', products_panel_view, name='panel_categorys'),
    path('panel/sales', products_panel_view, name='panel_sales'),

    path('panel/modify/<int:pk>/', modify_product_view, name='modify'),
    # path('panel/delete/<int:pk>', products_panel_view, name='delete'),

]