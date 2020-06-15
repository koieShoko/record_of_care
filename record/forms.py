from django import forms
from .models import *
class MealRecordForm(forms.ModelForm):
        class Meta:
                model = Meal_record
                fields = (
                        'resident',
                        'date',
                        'time',
                        'form1',
                        'form2',
                        'form3',
                        'notice',
                        'staff',
                        'translated_notice',
                )
                widgets = {
                        'translated_notice': forms.Textarea(attrs={'class': 'notice'}),
                        'notice': forms.Textarea(attrs={'class': 'notice'}),
                        'date': forms.DateInput(attrs={'class': 'date'}),
                        'time': forms.TimeInput(format='%H:%M'),
                        'staff':forms.HiddenInput(),
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
																											
