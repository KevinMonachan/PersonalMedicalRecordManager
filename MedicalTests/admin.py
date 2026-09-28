from django.contrib import admin
from .models import MedicalTests

class DoctorVisitsAdmin(admin.ModelAdmin):
    list_display =('user','TestName','TestDate')

admin.site.register(MedicalTests, DoctorVisitsAdmin)

# Register your models here.
