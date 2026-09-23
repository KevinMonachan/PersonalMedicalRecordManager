from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def consultation(request):
    return HttpResponse("<h1>Consultation</h1><p>This is the consultation page.</p>")
def diagnosis(request):
    return HttpResponse("<h1>Diagnosis</h1><p>This is the diagnosis page.</p>")
def Prescription(request):
    return HttpResponse("<h1>Prescription</h1><p>This is the prescription page.</p>");

