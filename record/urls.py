from django.urls import path
from . import views
urlpatterns=[
    path('residents/',views.residents_list,name='residents_list'),
    path('meal_record/read/',views.meal_record_read,name='meal_record_read'),
    path('meal_record/new/',views.meal_record_new,name='meal_record_new'),
    path('meal_record/translate/<int:pk>/',views.meal_record_translate,name='meal_record_translate'),
]
