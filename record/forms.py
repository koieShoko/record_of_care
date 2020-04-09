from django import forms
from .models import Meal_record
class MealRecordForm(forms.ModelForm):
        class Meta:
                model = Meal_record
                fields = (
                        'resident',
                        'staff',
                        'date',
                        'time',
                        'kind',
                        'staple_food',
                        'side_food',
                        'notice'
                )
