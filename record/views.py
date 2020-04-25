from django.shortcuts import render
from .models import Meal_record
from .forms import MealRecordForm
from django.utils import timezone
from record.models import Record
from django.shortcuts import redirect
from .translate import WordInfo, IikaeTango, Yomikomi, Translater, Kaigokiroku
import csv

def residents_list(request):
    a=1
    return render(request, 'record/residents_list.html',{'a':a})

def meal_record_new(request):
    if request.method =="POST":
        form=MealRecordForm(request.POST)
        if form.is_valid():
            meal_record=form.save(commit=False)#まだ保存しない
            meal_record.register()
            return redirect('meal_record_translate',pk=meal_record.pk)
    else:
        form=MealRecordForm()
    return render(request, 'record/meal_record_edit.html', {'form':form})


def meal_record_translate(request,pk):
#    string=Record.objects.get(pk=pk).notice
#    string1=string.replace('開口','口の開き')
#    translated_string=string1.replace('良好','よい')
    string=Record.objects.get(pk=pk).notice
    with open("/home/jinisuke55/record_of_care/record/string.csv","w") as f:
        writer=csv.writer(f)
        writer.writerow([string])
    kiroku=Kaigokiroku()
    translated_string=kiroku.translatedWords
    #translated_string=string.replace("仰臥位","上を見て寝る姿勢")
    return render(request, 'record/meal_record_translated.html', {'string':string,'translated_string':translated_string})



def meal_record_read(request):
    #if request.method =="POST":
    string=Record.objects.filter(date__iexact="2020-04-09")[0].notice
        #if form.is_valid():
         #   meal_record=form.save(commit=False)#まだ保存しない
          #  meal_record.residen
           # meal_record.written_date=timezone.now()
           # post.save()
    return render(request, 'record/meal_record_read.html', {'string':string})

