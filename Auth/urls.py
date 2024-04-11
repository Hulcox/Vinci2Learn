from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_index, name="login"),
    path('register/', register_index, name="register"),
    path('logout/', logout_index, name="logout"),
]