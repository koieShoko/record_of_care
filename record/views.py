from django.shortcuts import render
from .models import Meal_record
from .forms import *
from django.utils import timezone
from record.models import *
from django.shortcuts import redirect
from .translate import *
import csv


def meal_record_new(request):
    if request.method =="POST":
        form=MealRecordForm(request.POST)
        if form.is_valid():
            meal_record=form.save(commit=False)#まだ保存しない
            meal_record.staff=Staff.objects.get(username=request.user.username)
            meal_record.register()
            return redirect('translate',pk=meal_record.pk)
    else:
        form=MealRecordForm()
    return render(request, 'record/edit.html', {'form':form})


def translate(request,pk):
    string=Record.objects.get(pk=pk).notice
    kiroku=Translater(string)
    translated_string=kiroku.translated_text
    #セッション変数に保存
    request.session['translated_notice']=translated_string
    return render(request, 'record/translated.html', {'string':string,'translated_string':translated_string,'pk':pk})


def translate_save(request,pk):
    record=Record.objects.get(pk=pk)
    record.translated_notice=request.session['translated_notice']
    record.save()
    return redirect('/meal_record/new/')


def translate_rewrite(request,pk):
    if request.method == "POST":
        form=translated_notice_form(request.POST)
        if form.is_valid():
            record=Record.objects.get(pk=pk)
            record.translated_notice=request.POST['translated_notice']
            record.save()
        return redirect('/meal_record/new/')
    else:
        translated_notice=request.session['translated_notice']
        form = translated_notice_form(initial={'translated_notice':translated_notice} )
    return render(request,'record/edit.html',{'form':form})


def meal_record_read(request):
    #if request.method =="POST":
    string=Record.objects.filter(date__iexact="2020-04-09")[0].notice
        #if form.is_valid():
         #   meal_record=form.save(commit=False)#まだ保存しない
          #  meal_record.residen
           # meal_record.written_date=timezone.now()
           # post.save()
    return render(request, 'record/meal_record_read.html', {'string':string})

