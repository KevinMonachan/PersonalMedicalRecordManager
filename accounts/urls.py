from django.urls import path
from . import views

urlpatterns =[
    path('',views.login_view,name="login"),
    path('dashboard/',views.dashboard),
    path('register/',views.registration_view,name="register")
]