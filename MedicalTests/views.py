from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Registration(request):
    return render(request,'Testform.html')

