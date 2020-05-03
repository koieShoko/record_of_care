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
                        'notice'
                )
                widgets = {
                        'date': forms.SelectDateWidget,
                        'time': forms.TimeInput(format='%HH:%MM'),
                }

class translated_notice_form(forms.ModelForm):
        class Meta:
                model =Record
                fields = (
                        'translated_notice',
                )
                
