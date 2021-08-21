
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('UI.urls')),
    path('rc/',include('riddleComp.urls')),
    path('back/',include('back_end.urls'))    
]