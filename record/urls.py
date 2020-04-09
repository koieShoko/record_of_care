from django.urls import path
from . import views
urlpatterns=[
    path('residents/',views.residents_list,name='residents_list'),
    path('meal_record/read/',views.meal_record_read,name='meal_record_read')

]
