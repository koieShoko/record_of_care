from django import forms
from .models import Meal_record, Record
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


																											
class SearchRecordForm(forms.ModelForm):
        class Meta:
                model = Record 
                fields=(
                        'date',
                )																													
																											
																																																				
																											
