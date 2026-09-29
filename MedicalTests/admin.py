from django.contrib import admin
from .models import MedicalTests

class MedicalTestsAdmin(admin.ModelAdmin):
    list_display =('user','TestName','TestDate')

admin.site.register(MedicalTests, MedicalTestsAdmin)

# Register your models here.
