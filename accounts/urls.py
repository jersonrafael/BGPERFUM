from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login_view),
<<<<<<< HEAD
    path("logout_view/", logout_view, name="")
=======
    # path("register/", register_view),
    path("logout/", logout_view, name="logout_view"),
>>>>>>> routes
]
