from django.contrib import admin
from .models import Resident
from .models import Staff
from .models import Meal_record


admin.site.register(Resident)
admin.site.register(Staff)

admin.site.register(Meal_record)
