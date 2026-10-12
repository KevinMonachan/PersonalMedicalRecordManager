from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.models import User

# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','').strip()
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')

        if not username or not password:
            messages.error(request,'Username and Password are required.')
            return render(request,'registration/register.html')
        if confirm_password != password:
            messages.error(request,'Passwords do not match.')
            return render(request,'registration/register.html')
        if User.objects.filter(username = username).exists():
            messages.error(request,'Username exist already')
            return render(request,'registration/register.html')
        user = User.objects.create_user(
            username = username,
            password = password
        )
        messages.success(request,'Registration successfully.Please Login')
        return redirect('login')
    return render(request,'registration/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

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

    