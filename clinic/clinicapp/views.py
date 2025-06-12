from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import MedicalProfessional, Occupation
from .forms import MedicalProfessionalForm, UserRegisterForm, LoginForm

# Home page view
@login_required
def home(request):
    return render(request, 'home.html')

# User registration
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

# User login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# User logout
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

# Dashboard view (protected)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Doctors list view
@login_required
def doctors(request):
    doctors_list = MedicalProfessional.objects.select_related('occupation').all()
    return render(request, 'doctors.html', {'doctors': doctors_list})

# Doctor profile view
@login_required
def doctor_profile(request, doctor_id):
    medical_professional = get_object_or_404(MedicalProfessional, pk=doctor_id)
    return render(request, 'doctor-profile.html', {'medical_professional': medical_professional})

# Add doctor view
@login_required
def add_doctor(request):
    occupations = Occupation.objects.all()

    if request.method == 'POST':
        form = MedicalProfessionalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor added successfully! 🎉")
            return redirect('doctors')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MedicalProfessionalForm()

    return render(request, 'add-doctor.html', {
        'form': form,
        'occupations': occupations
    })

# Edit doctor view
@login_required
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(MedicalProfessional, pk=doctor_id)
    if request.method == 'POST':
        form = MedicalProfessionalForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor updated successfully! ✅")
            return redirect('doctors')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MedicalProfessionalForm(instance=doctor)

    return render(request, 'edit-doctor.html', {
        'form': form,
        'doctor': doctor
    })

# Delete doctor view
@login_required
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(MedicalProfessional, pk=doctor_id)
    try:
        doctor.delete()
        messages.success(request, "Doctor deleted successfully! 🗑️")
    except Exception as e:
        messages.error(request, f"Error deleting doctor: {str(e)}")
    return redirect('doctors')

# Add occupation view
@login_required
def add_occupation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Occupation.objects.create(name=name)
            messages.success(request, "Occupation added successfully! ✅")
            return redirect('add_doctor')
        else:
            messages.error(request, "Occupation name is required.")
    return render(request, 'add-occupation.html')
