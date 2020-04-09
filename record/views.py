from django.shortcuts import render
from .models import Meal_record
from .forms import MealRecordForm
from django.utils import timezone
from record.models import Record

def residents_list(request):
    a=1
    return render(request, 'record/residents_list.html',{'a':a})

#def meal_record_new(request):
    #if request.method =="POST":
 #   form=MealRecordForm()
        #if form.is_valid():
         #   meal_record=form.save(commit=False)#まだ保存しない
          #  meal_record.residen
           # meal_record.written_date=timezone.now()
           # post.save()
  #  return render(request, 'record/meal_record_edit.html', {'form':form})





def meal_record_read(request):
    #if request.method =="POST":
    string=Record.objects.filter(date__iexact="2020-04-09")[0].notice
        #if form.is_valid():
         #   meal_record=form.save(commit=False)#まだ保存しない
          #  meal_record.residen
           # meal_record.written_date=timezone.now()
           # post.save()
    return render(request, 'record/meal_record_read.html', {'string':string})
