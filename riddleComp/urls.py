from .views import *
from django.urls import path

urlpatterns = [
    path ('<str:r_id>/', riddle)
]
