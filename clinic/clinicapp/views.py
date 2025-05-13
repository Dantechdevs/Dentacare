from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Doctor

def home(request):
    return render(request, 'home.html')

def doctors(request):
    doctors_list = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors_list})

def add_doctor(request):
    occupations = Doctor.OCCUPATION_CHOICES
    
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
            Doctor.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST.get('last_name', ''),
                email=request.POST['email'],
                phone=request.POST['phone'],
                occupation=request.POST['occupation'],
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

def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    occupations = Doctor.OCCUPATION_CHOICES
    
    if request.method == 'POST':
        try:
            doctor.first_name = request.POST['first_name']
            doctor.last_name = request.POST.get('last_name', '')
            doctor.email = request.POST['email']
            doctor.phone = request.POST['phone']
            doctor.occupation = request.POST['occupation']
            doctor.bio = request.POST.get('bio', '')
            doctor.address = request.POST.get('address', '')
            doctor.county = request.POST.get('county', '')  # Corrected here
            
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

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    try:
        doctor.delete()
        messages.success(request, "Doctor deleted successfully! 🗑️")
    except Exception as e:
        messages.error(request, f"Error deleting doctor: {str(e)}")
    return redirect('doctors')

def dashboard(request) :
    return render(request, 'dashboard.html')