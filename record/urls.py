from django.urls import path
from . import views
urlpatterns=[
    path('meal_record/read/',views.meal_record_read,name='meal_record_read'),
    path('check_translate/',views.check_translate,name='check_translate'),
    path('translate/<int:pk>/save/',views.translate_save,name='translate_save'),
    path('translate/rewrite/<int:pk>/',views.translate_rewrite,name='translate_rewrite'),
    path('meal_record/new/',views.meal_record_new,name='meal_record_new'),
 
    path('',views.meal_record_new,name='meal_record_new'),

]
