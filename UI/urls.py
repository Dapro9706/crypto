from .views import home, redirect_home
from django.urls import path

urlpatterns = [
    path ('home/', home),
    path ('', redirect_home)
]
