from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MedicalTests(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    TestName = models.CharField(max_length=100)
    TestDate = models.DateField()
    Result = models.TextField()
    notes = models.TextField(blank=True)
    Report = models.FileField(upload_to='reports/',blank=True)
    
