from django.urls import path
from . import views
urlpatterns = [
    path('medicaltestview',views.medicaltest_view,name ='medicaltestview'),
    path('medicaltestfill',views.medicaltestfill_view,name = 'medicaltestfill')
]