from django import forms
from .models import *
from record.views import *


class RecordForm(forms.ModelForm):
        class Meta:
                model  = Record
                fields = (
                        'resident',
                        'date',
                        'time',
                        'form0',
                        'form1',
                        'form2',
                        'form3',
                        'notice',
                        'translated_notice',
                )
                widgets = {
                        'translated_notice' : forms.Textarea(attrs={'class': 'notice'}),
                        'notice'            : forms.Textarea(attrs={'class': 'notice'}),
                        'date'              : forms.DateInput(attrs={'class': 'date'}),
                        'time'              : forms.TimeInput(format='%H:%M'),
                        'staff'             : forms.HiddenInput(),
                        'form0'             : forms.HiddenInput(),
                        'form1'             : forms.Select(attrs={'name':'form1'}),
                        'form2'             : forms.Select(attrs={'name':'form2'}),
                        'form3'             : forms.Select(attrs={'name':'form3'}),                    
                }
        def __init__(self, *args, **kwargs):
                kwargs.setdefault('label_suffix', '')
                super().__init__(*args, **kwargs)

class RecordForm_ForWriteAll(forms.ModelForm):
        class Meta:
                model = Record
                fields = (
                        'date',
                        'time',
                        'form0',
                        'form1',
                        'form2',
                        'form3',
                        'notice',
                )
                widgets = {
                        'notice': forms.Textarea(attrs   = {'class': 'notice'}),
                        'date'  : forms.DateInput(attrs  = {'class': 'date'}),
                        'time'  : forms.TimeInput(format = '%H:%M'),
                        'form0' : forms.HiddenInput(),
                        'form1' : forms.Select(attrs = {'id':"form1"}),
                        'form2' : forms.Select(),
                        'form3' : forms.Select(),                    
                }
        def __init__(self, *args, **kwargs):
                kwargs.setdefault('label_suffix', '')
                super().__init__(*args, **kwargs)

																											
class SearchRecordForm(forms.ModelForm):
        class Meta:
                model = Record 
                fields=(
                        'date',
                )																													
																											
class SearchResidentForm(forms.Form):
        resident = forms.MultipleChoiceField(
                label = "入居者",
                required = False,
                disabled = False,
                widget   = forms.CheckboxSelectMultiple(
                        attrs={
                                'class': 'resident'
                        }
                )
        )        																																															
																									

class SelectKindForm(forms.ModelForm):
        class Meta:
                model = Record
                fields=(
                        'form0',
                )
