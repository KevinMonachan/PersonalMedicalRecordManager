from django.contrib import admin
from .models import DoctorVisits

# Register your models here.
class DoctorVisitsadmin(admin.ModelAdmin):
    list_display = ('DoctorName','Hospital','visitDate')

admin.site.register(DoctorVisits,DoctorVisitsadmin)    


