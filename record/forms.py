from django import forms
from .models import Meal_record, Record
class MealRecordForm(forms.ModelForm):
        class Meta:
                model = Meal_record
                fields = (
                        'resident',
                        'date',
                        'time',
                        'kind',
                        'staple_food',
                        'side_food',
                        'notice',
                        'staff',
                        'translated_notice',
                        'written_date',
                )
                widgets = {
                        'translated_notice': forms.Textarea(attrs={'class': 'notice'}),
                        'notice': forms.Textarea(attrs={'class': 'notice'}),
                        'date': forms.DateInput(attrs={'class': 'date'}),
                        'time': forms.TimeInput(format='%H:%M'),
                        'staff':forms.HiddenInput(),
                        'written_date':forms.HiddenInput(),
                }




class translated_notice_form(forms.ModelForm):
        class Meta:
                model =Record
                fields = (
                        'translated_notice',
                )
                
