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
    residents=request.session.get('checked_residents')
    request.session["checked_residents"]=[]
    countResidents=len(residents)
    MealRecordFormSet = modelformset_factory(
        Meal_record,
        form=MealRecordForm,
        extra=countResidents,
        max_num=20,
    )
    dict_to_write_all=request.session['dict_to_write_all']
    request.session['dict_to_write_all']={}
    initial=[
        {
        "resident": Resident.objects.get(full_name=residents[i]),
        "staff"   : request.user,
        }for i in range(0,countResidents)
    ]
    for x in initial:
        x.update(dict_to_write_all)
    submit_text="記入完了"
    if request.method =="POST":
        formset=MealRecordFormSet(request.POST)
        if formset.is_valid():
            instances=formset.save(commit=False)
            i=0
            for file in instances:
                postKey="form-"+str(i)+"-notice"
                file.translated_notice=wakatigaki(Translater(request.POST[postKey]).translated_text)
                file.register()
                i+=1
            return redirect('check_translate')
    else:
        formset=MealRecordFormSet(initial=initial,queryset=Meal_record.objects.none())
    return render(request, 'record/edit.html', {'formset':formset,'submit_text':submit_text})

def write_all(request):
    title="まとめて入力する"
    submit_text="入力完了"
    if request.method == "POST":
        form=MealRecordForm_ForWriteAll(request.POST)                
        if form.is_valid():
            labels=[
                        'date',
                        'time',
                        'form1',
                        'form2',
                        'form3',
                        'notice',]
            dict_to_write_all={}
            for label in labels:
                dict_to_write_all[str(label)]=request.POST[str(label)]
            request.session["dict_to_write_all"]=dict_to_write_all
        return redirect('/meal_record/new')
    else:
        form = MealRecordForm_ForWriteAll()
        return render(request, 'record/search.html', {
            'form':form, 
            'submit_text':submit_text,
            'title':title,
        })


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
        #今回変換したレコードを以降表示しない
        records=Meal_record.objects.filter(isTranslated=False)
        records.update(isTranslated=True)
        return redirect('/record/search')
    else:
        formset=MealRecordFormSet(queryset=Meal_record.objects.filter(isTranslated=False))
        return render(request, 'record/edit.html', {'formset':formset,'submit_text':submit_text})



def search_record(request):
    title = "記録を選ぶ"
    submit_text="読む"
    if request.method == "POST":
        form=SearchRecordForm(request.POST)                
        records=[]
        if form.is_valid():
            date=request.POST["date"]
            department=request.user.department
            records=Meal_record.objects.filter(date=date, department=department).order_by('room','date','time')
            labels=["名前","日付","時刻","種類","主食量","副食量","特記事項"]
            if request.user.reading_support == True:
                labels=["名前","日にち","時間","種類","ご飯","ご飯以外","何があったか"] 
        return render(request, 'record/read.html', {'records': records, 'labels':labels})
    else:
        form = SearchRecordForm()
        return render(request, 'record/search.html', {
            'form':form, 
            'submit_text':submit_text,
            'title':title,
        })

def search_resident(request):
    title   = '利用者を選択する'
    submit_text="選択完了"
    results = {}
    if request.method == "POST":
        request.session['checked_residents']=request.POST.getlist('resident')
        return redirect('/write_all')
    else:
        form = SearchResidentForm()
        choice =[
            (resident, resident.full_name) for resident in Resident.objects.filter(department=request.user.department) 
        ]
        form.fields['resident'].choices = choice
        form.fields['resident'].initial = [x for x in Resident.objects.filter(department=request.user.department)] 
        return render(
            request, 
            'record/search.html', 
            {'form':form, 'submit_text':submit_text, 'title':title}
        )

def change_mode(request):
    staff_pk         = request.user.staff.pk
    previous_support = request.user.staff.reading_support
    next_support     = not(previous_support)
    staff=Staff.objects.get(pk=staff_pk)
    staff.reading_support=next_support
    staff.save()
    return redirect(request.META['HTTP_REFERER'])




