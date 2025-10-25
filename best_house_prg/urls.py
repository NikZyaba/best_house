from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.main.urls")),
    path("projects/", include("apps.our_projects.urls")),
    path("user/", include("apps.user.urls", namespace="user")),
    path('admin/', admin.site.urls),
]
