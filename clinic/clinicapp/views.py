from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MedicalProfessional, Occupation

# Home page view
def home(request):
    return render(request, 'home.html')

# Doctors list view
def doctors(request):
    doctors_list = MedicalProfessional.objects.select_related('occupation').all()
    return render(request, 'doctors.html', {'doctors': doctors_list})

# Doctor profile view
def doctor_profile(request, doctor_id):
    medical_professional = get_object_or_404(MedicalProfessional, pk=doctor_id)
    return render(request, 'doctor-profile.html', {'medical_professional': medical_professional})

# Add doctor view
def add_doctor(request):
    occupations = Occupation.objects.all()

    if request.method == 'POST':
        required_fields = {
            'first_name': 'First name is required',
            'email': 'Email address is required',
            'phone': 'Phone number is required',
            'occupation': 'Occupation is required'
        }

        errors = []
        for field, message in required_fields.items():
            if not request.POST.get(field):
                errors.append(message)

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('add_doctor')

        try:
            occupation_id = request.POST.get('occupation')
            occupation = get_object_or_404(Occupation, pk=occupation_id)

            MedicalProfessional.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST.get('last_name', ''),
                email=request.POST['email'],
                phone=request.POST['phone'],
                occupation=occupation,
                bio=request.POST.get('bio', ''),
                address=request.POST.get('address', ''),
                county=request.POST.get('county', ''),
                avatar=request.FILES.get('avatar')
            )
            messages.success(request, "Doctor added successfully! 🎉")
            return redirect('doctors')

        except Exception as e:
            messages.error(request, f"Error saving doctor: {str(e)}")
            return redirect('add_doctor')

    return render(request, 'add-doctor.html', {'occupations': occupations})

# Edit doctor view
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(MedicalProfessional, pk=doctor_id)
    occupations = Occupation.objects.all()

    if request.method == 'POST':
        try:
            occupation_id = request.POST.get('occupation')
            occupation = get_object_or_404(Occupation, pk=occupation_id)

            doctor.first_name = request.POST['first_name']
            doctor.last_name = request.POST.get('last_name', '')
            doctor.email = request.POST['email']
            doctor.phone = request.POST['phone']
            doctor.occupation = occupation
            doctor.bio = request.POST.get('bio', '')
            doctor.address = request.POST.get('address', '')
            doctor.county = request.POST.get('county', '')

            if 'avatar' in request.FILES:
                doctor.avatar = request.FILES['avatar']

            doctor.save()
            messages.success(request, "Doctor updated successfully! ✅")
            return redirect('doctors')

        except Exception as e:
            messages.error(request, f"Error updating doctor: {str(e)}")
            return redirect('edit_doctor', doctor_id=doctor_id)

    return render(request, 'edit-doctor.html', {
        'doctor': doctor,
        'occupations': occupations
    })

# Delete doctor view
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(MedicalProfessional, pk=doctor_id)
    try:
        doctor.delete()
        messages.success(request, "Doctor deleted successfully! 🗑️")
    except Exception as e:
        messages.error(request, f"Error deleting doctor: {str(e)}")
    return redirect('doctors')

# Dashboard view
def dashboard(request):
    return render(request, 'dashboard.html')

# Add occupation view
def add_occupation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Occupation.objects.create(name=name)
            messages.success(request, "Occupation added successfully! ✅")
            return redirect('add_doctor')
        else:
            messages.error(request, "Occupation name is required.")
            return redirect('add_occupation')

    return render(request, 'add-occupation.html')
