from django.urls import path
from . import views
        
urlpatterns = [
    path('', views.home, name='home'),
    path('doctors.html', views.doctors, name='doctors'),
    path('add-doctor.html', views.add_doctor, name='add_doctor'),
    path('edit-doctor/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('delete-doctor/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path('dashboard.html', views.dashboard, name='dashboard'),
]
