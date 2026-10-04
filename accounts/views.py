from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

# Create your views here.
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username = username ,
            password = password
        )

        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid details")
    return render(request,'registration/login.html')
@login_required
def dashboard(request):
    return render(request,'dashboard.html')    

def registration_view(request):
    return render(request,'registration/register.html')
    
def logout_view(request):
    logout(request)
    return redirect("login") 