from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def doctors(request):
    return render(request, 'doctors.html',{})

def add_doctor(request):
    return render(request, 'add-doctor.html',{})    
