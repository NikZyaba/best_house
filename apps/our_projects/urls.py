from django.urls import path
from . import views

app_name = "our_projects"

urlpatterns = [
    path('our_projects/', views.our_projects, name='our_projects'),
]
