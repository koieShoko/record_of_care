from django.contrib import admin
from .models import Resident
from .models import Staff
from .models import Record


admin.site.register(Resident)
admin.site.register(Staff)

admin.site.register(Record)
