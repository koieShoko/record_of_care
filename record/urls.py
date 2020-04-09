from django.urls import path
from . import views
urlpatterns=[
    path('resident/',views.residents_list,name='residents_list'),
    path('meal_record/new/',views.meal_record_new, name='meal_record_new'),
]

