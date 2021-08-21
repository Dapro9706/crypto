from django.urls import path
from .views import crypto

urlpatterns = [
    path ('crypto/', crypto)
]
