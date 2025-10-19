from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main, name='main'),
    path('get_consult', views.get_consult, name="get_consult"),
    path('calculate/', views.calculate_prj, name='calculate_project'),
    path('successconsulting/', views.success_consultation, name='success_consultation'),
    path('successcalculation/', views.success_calculation, name='success_calculation'),
    # Отзывы
    path('reviews/', views.reviews, name='reviews'),
    path('reviews/review/', views.review_form, name='review_form'),  # форма ввода
    path('reviews/review/thanks/', views.reviews_rating, name='reviews_rating'),  # страница благодарности
]
