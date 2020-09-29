from django.shortcuts import render
from .models import *
from .forms import *
from django.forms import modelformset_factory, ModelForm
from django.utils import timezone
from record.models import *
from record.ruby import Ruby_maker
from django.shortcuts import redirect
from django.db.models import Subquery
from .translate import *
from django.utils.html import mark_safe
import csv




def search_resident(request):
    title       = 'ステップ1:   入居者を選ぶ'
    explain     = None
    submit_text = "選択完了"
    results     = {}
    if request.method == "POST":
        request.session['checked_residents']=request.POST.getlist('resident')
        return redirect('/select_kind')
    else:#初回
        form = SearchResidentForm()
        choice =[
            (resident, resident.full_name) for resident in Resident.objects.filter(department=request.user.department,is_leaving=False) 
        ]
        form.fields['resident'].choices = choice
        form.fields['resident'].initial = [x for x in Resident.objects.filter(department=request.user.department)] 
        return render(
            request, 
            'record/search.html', 
            {
                'form'          : form,
                'submit_text'   : submit_text,
                'title'         : title,
                'explain'       : explain,
             }
        )

def select_kind(request):
    title       = 'ステップ2:   記録の種類を選ぶ'
    explain     = None
    submit_text = "選択完了"
    results     = {}
    if request.method == "POST":
        request.session['selected_kind'] =request.POST["form0"]
        return redirect('/write_all')
    else:#初回
        form = SelectKindForm()
        return render(
            request, 
            'record/search.html', 
            {
                'form'          : form,
                'submit_text'   : submit_text,
                'title'         : title,
                'explain'       : explain,
             }
        )

def write_all(request):
    form0_id = request.session["selected_kind"] 
    category_form0 = Category_form0.objects.get(id=form0_id)
    title       = "ステップ3:   全員に共通する部分を書く"
    explain     = str(category_form0) + "の記録"
    submit_text = "入力完了"
    if request.method == "POST":
        form=RecordForm_ForWriteAll(request.POST)                
        if form.is_valid():
            labels=[
                        'date', 
                        'time', 
                        'form0', 
                        'form1', 
                        'form2', 
                        'form3', 
                        'notice', 
                    ]
            dict_to_write_all={}
            for label in labels:
                if label in request.POST :
                    dict_to_write_all[str(label)]=request.POST[str(label)]
            request.session["dict_to_write_all"]=dict_to_write_all
        return redirect('/record/new')
    else:#初回
        form = RecordForm_ForWriteAll()
        form.fields['form0'].initial = form0_id
        form.fields['form1'].label = category_form0.form1_name
        form.fields['form2'].label = category_form0.form2_name
        form.fields['form3'].label = category_form0.form3_name
        form.fields['form1'].queryset = Category_form1.objects.filter(parent = category_form0)
        form.fields['form2'].queryset = Category_form2.objects.filter(parent = category_form0)
        form.fields['form3'].queryset = Category_form3.objects.filter(parent = category_form0)
        return render(
            request,
            'record/search.html',
            {
                'form':form, 
                'submit_text':submit_text,
                'title':title,
                'explain':explain,
            }
        )



def record_new(request):
    form0_id = request.session["selected_kind"] 
    category_form0 = Category_form0.objects.get(id=form0_id)
    title       = 'ステップ4:   各入居者の記録を書く'
    explain     = str(category_form0) + "の記録"
    submit_text = "やさしい日本語へ変換"
    residents   = request.session.get('checked_residents')
    request.session["checked_residents"]=[]
    countResidents    = len(residents)
    RecordFormSet = modelformset_factory(
        Record,
        form    = RecordForm,
        extra   = countResidents,
        max_num = 20,
    )
    dict_to_write_all=request.session['dict_to_write_all']
    request.session['dict_to_write_all']={}
    initial=[
        {   
            "form0"   : category_form0,
            "resident": Resident.objects.get(full_name=residents[i]),
            "staff"   : request.user,
        }
        for i in range(0,countResidents)
    ]
    for x in initial:
        x.update(dict_to_write_all)
    if request.method =="POST":#2回目
        formset=RecordFormSet(request.POST)
        if formset.is_valid():
            instances=formset.save(commit=False)
            i=0
            ruby_maker=Ruby_maker()
            for file in instances:
                postKey="form-"+str(i)+"-notice"
                file.translated_notice = Translater(request.POST[postKey]).translated_text
                file.ruby_translated_notice = ruby_maker.output(file.translated_notice)
                file.register()
                i+=1
            return redirect('check_translate')
        else:
            return render(
                request,
                'record/error.html'
                )
    else:#初回
        formset=RecordFormSet(initial=initial,queryset=Record.objects.none())
        form1 = category_form0.form1_name
        form2 = category_form0.form2_name
        form3 = category_form0.form3_name
        labels = ["名前","時刻","種類", form1, form2, form3 ,"特記事項", "特記事項（変換後）"]
        request.session["edit_labels"] = labels
        return render(
            request,
            'record/edit.html',
            {
                'formset'       :formset,
                'labels'        :labels,
                'submit_text'   :submit_text,
                'title'         :title,
                'explain'       :explain
            }
        )

def check_translate(request):
    form0_id = request.session["selected_kind"] 
    category_form0 = Category_form0.objects.get(id=form0_id)
    title       = 'ステップ5:   誤訳を修正する'
    explain     = str(category_form0) + "の記録"
    submit_text = "誤訳修正完了"
    RecordFormSet = modelformset_factory(
        Record,
        form    = RecordForm,
        extra   = 0,
        max_num = 20,
    )
    if request.method =="POST":
        formset=RecordFormSet(request.POST)
        formset.save()
        #今回変換したレコードを以降表示しない
        records=Record.objects.filter(isTranslated=False)
        records.update(isTranslated=True)
        return redirect('/record/search')
    else:
        formset=RecordFormSet(queryset=Record.objects.filter(isTranslated=False))
        return render( request, 'record/edit.html', {
                'formset'       : formset,
                'labels'        : request.session["edit_labels"],
                'submit_text'   : submit_text,
                'title'         : title,
                'explain'       : explain,
        })



def search_record(request):
    title   = "ステップ1:   記録を選ぶ"
    explain = ''
    submit_text="読む"
    ruby_translated_notice= []
    if request.method == "POST":
        form=SearchRecordForm(request.POST)                
        records=[]
        if form.is_valid():
            date = request.POST["date"]
            department = request.user.department
            records = Record.objects.filter(date=date, department=department).order_by('room','date','time')
            labels = ["名前","時刻","種類", "情報1", "情報2", "情報3" ,"特記事項","職員"]
            if request.user.reading_support == True:
                labels=["名前","時間","種類","情報1", "情報2", "情報3" ,"何があったか","書いた人"] 
            from record.html_maker import Date_formatter, Html_maker
            html_maker = Html_maker()
            df = Date_formatter()
            date_ja = df.date_translate_to_ja(date)
            title   = "ステップ2：記録を読む"
            explain =html_maker.make_ul(
                id = "base_explain",
                labels = ["日付：", "場所："],
                values = [date_ja, request.user.department + "階"]
            )
        else:
            return render(
                request,
                'record/error.html'
            )
        return render(request,'record/read.html',{
                'records'                : records,
                'labels'                 : labels,
                'title'                  : title,
                'explain'                : mark_safe(explain)
        })
    else:#初回
        form = SearchRecordForm()
        return render(request, 'record/search.html', {
                'form'          : form, 
                'title'         : title,
                'explain'       : explain,
                'submit_text'   : submit_text,
        })

def change_mode(request):
    staff_pk         = request.user.staff.pk
    previous_support = request.user.staff.reading_support
    next_support     = not(previous_support)
    staff=Staff.objects.get(pk=staff_pk)
    staff.reading_support=next_support
    staff.save()
    return redirect(request.META['HTTP_REFERER'])




