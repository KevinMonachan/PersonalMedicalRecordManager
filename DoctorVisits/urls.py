from django.urls import path
from . import views

urlpatterns = [
    path('consultation',views.consultation, name='consultation'),
    path('diagnosis',views.diagnosis, name='diagnosis'),
    path('prescription',views.Prescription, name='prescription')
]