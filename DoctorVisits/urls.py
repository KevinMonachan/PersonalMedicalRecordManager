from django.urls import path
from . import views

urlpatterns = [
    path('consultation',views.Consultation,name="consultation"),
    path('diagnosis',views.Diagnosis,name="Diagnosis"),
    path('prescriptions',views.Prescription,name = "Prescription"),   
]