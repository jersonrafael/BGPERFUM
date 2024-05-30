from django.urls import path
from .views import *

urlpatterns = [
    path('', categorys_panel_view, name='panel_categorys'),
    path('category/<int:pk>/', category_panel_view, name='panel_category'),
    path('add/category/', create_category_view, name='panel_create_category'),
    path('edit/category/<int:pk>/', edit_category_view, name='panel_category'),
    path('del/category/<int:pk>/', delete_category_panel_view, name='delete_panel_category'),
]