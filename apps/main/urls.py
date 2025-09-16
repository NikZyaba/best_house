from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main, name='main'),
    path('/get_consult', views.get_consult, name="get_consult"),
]