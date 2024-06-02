from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login_view),
    path("logout_view/", logout_view, name="")
]
