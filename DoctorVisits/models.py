from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DoctorVisits(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    DoctorName = models.CharField(max_length=100)
    Hospital = models.CharField(max_length= 100)
    visitDate = models.DateField()
    Reason = models.TextField(blank=True)
    Diagnosis=models.TextField(blank=True)
    Prescription = models.TextField(blank=True)
    Notes = models.TextField(blank = True)
    Result = models.FileField(upload_to='result/',blank= True)
