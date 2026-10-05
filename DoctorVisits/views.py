from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def doctorvisit_view(request):
    return render(request,'doctorvisit/doctorvisitview.html')
def doctorvisitform_view(request):
    return render(request,'doctorvisit/doctorvisitform.html')


