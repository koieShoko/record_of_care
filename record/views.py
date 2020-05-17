from django.shortcuts import render
from .models import *
from .forms import *
from django.forms import modelformset_factory, ModelForm
from django.utils import timezone
from record.models import *
from django.shortcuts import redirect
from django.db.models import Subquery
from .translate import *
import csv



def meal_record_new(request):
    countResidents=3
    MealRecordFormSet = modelformset_factory(
        Meal_record,
        form=MealRecordForm,
        extra=countResidents,
        max_num=20,
    )
    initial=[
        {
        "resident":Resident.objects.get(pk= i),
        "staff":request.user,
        "written_date":timezone.now(),}
         for i in range(1,countResidents + 1 )
    ]
    submit_text="記入完了"
    if request.method =="POST":
        formset=MealRecordFormSet(request.POST)
        if formset.is_valid():
            instances=formset.save(commit=False)
            i=0
            for file in instances:
                postKey="form-"+str(i)+"-notice"
                file.translated_notice=Translater(request.POST[postKey]).translated_text
                file.save()
                i+=1
            return redirect('check_translate')
    else:
        formset=MealRecordFormSet(initial=initial,queryset=Meal_record.objects.none())
    return render(request, 'record/edit.html', {'formset':formset,'submit_text':submit_text})



def check_translate(request):
    MealRecordFormSet = modelformset_factory(
        Meal_record,
        form=MealRecordForm,
        extra=0,
        max_num=20,
    )
    submit_text="誤訳修正完了"
    if request.method =="POST":
        formset=MealRecordFormSet(request.POST)
        formset.save()
        return redirect('meal_record_new')
    else:
        formset=MealRecordFormSet(queryset=Meal_record.objects.order_by("written_date").reverse()[:3])
        return render(request, 'record/edit.html', {'formset':formset,'submit_text':submit_text})


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
        residents=Staff.objects.all()
    return render(request,'record/edit.html',{'form':form,'residents':residents} )


def meal_record_read(request):
    #if request.method =="POST":
    string=Record.objects.filter(date__iexact="2020-04-09")[0].notice
        #if form.is_valid():
         #   meal_record=form.save(commit=False)#まだ保存しない
          #  meal_record.residen
           # meal_record.written_date=timezone.now()
           # post.save()
    return render(request, 'record/meal_record_read.html', {'string':string})

