from django.urls import path
from .views import *

urlpatterns = [
    path('', statistic_index, name="statistic"),
]