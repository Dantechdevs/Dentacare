
from django.urls import path
from . import views
        
urlpatterns = [
    path('', views.home, name='home'),
    path('doctors.html', views.doctors, name='doctors'),
    path('add-doctor.html', views.add_doctor, name='add_doctor'),
]
