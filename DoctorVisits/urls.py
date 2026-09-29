from django.urls import path
from . import views

urlpatterns = [
    path('visitform',views.visitform, name='visitform'),
]