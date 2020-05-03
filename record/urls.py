from django.urls import path
from . import views
urlpatterns=[
    path('',views.meal_record_new,name='meal_record_new'),

    path('meal_record/read/',views.meal_record_read,name='meal_record_read'),
    path('meal_record/new/',views.meal_record_new,name='meal_record_new'),
    path('translate/<int:pk>/',views.translate,name='translate'),
    path('translate/<int:pk>/save/',views.translate_save,name='translate_save'),
    path('translate/rewrite/<int:pk>/',views.translate_rewrite,name='translate_rewrite'),


]
