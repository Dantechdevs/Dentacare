from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor

def home(request):
    return render(request, 'home.html')

def doctors(request):
    return render(request, 'doctors.html')

def add_doctor(request):
    if request.method == 'POST':
        required_fields = {
            'first_name': 'First name is required',
            'email': 'Email address is required',
            'phone': 'Phone number is required'
        }
        
        # Validate required fields
        errors = []
        for field, message in required_fields.items():
            if not request.POST.get(field):
                errors.append(message)
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('add_doctor')
        
        try:
            # Create doctor with form data
            Doctor.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST.get('last_name', ''),  # Optional field
                email=request.POST['email'],
                phone=request.POST['phone'],
                bio=request.POST.get('bio', ''),
                avatar=request.FILES.get('avatar')  # Handle file upload
            )
            messages.success(request, "Doctor added successfully! 🎉")
            return redirect('add_doctor')
            
        except Exception as e:  # Catch database errors
            messages.error(request, f"Error saving doctor: {str(e)}")
            return redirect('add_doctor')

    return render(request, 'add-doctor.html')
