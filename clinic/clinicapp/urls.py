from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Doctor management
    path('doctors.html', views.doctors, name='doctors'),
    path('doctor/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
    path('add-doctor.html', views.add_doctor, name='add_doctor'),
    path('edit-doctor/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('delete-doctor/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    

    # Dashboard and Occupations
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('add-occupation/', views.add_occupation, name='add_occupation'),
    
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]


