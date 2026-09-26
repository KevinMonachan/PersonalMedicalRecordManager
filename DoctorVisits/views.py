from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Consultation(request):
    return HttpResponse("<h1>Consultation</h1><p>This is Consultation Page</p>")
def  Diagnosis(request):
    return HttpResponse("<h1>Diagnosis</h1><p>This is Diagnosis Page</p>")
def Prescription(request):
    return HttpResponse("<h1>Prescription</h1><p>This is Prescription Page")
