from django.urls import path
from . import views

urlpatterns = [
    path('doctorvisit/',views.doctorvisit_view, name='doctorvisit'),
    path('doctorvisitform',views.doctorvisitform_view,name = "doctorvisitform")
]