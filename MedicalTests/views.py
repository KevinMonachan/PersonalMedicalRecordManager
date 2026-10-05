from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def medicaltest_view(request):
    return render(request,'medicaltest/medicaltest.html')
def medicaltestfill_view(request):
    return render(request,'medicaltest/fill.html')

