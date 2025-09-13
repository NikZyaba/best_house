
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.main.urls", namespace="main")),
    path("", include("apps.user.urls", namespace="user")),
    path('admin/', admin.site.urls),
    
]
