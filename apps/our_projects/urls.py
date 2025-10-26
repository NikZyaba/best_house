from django.urls import path
from . import views

app_name = "our_projects"

urlpatterns = [
    path('', views.our_projects, name='our_projects'),
    path('add/', views.add_project, name='add_project'),
]
