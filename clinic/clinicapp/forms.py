from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MedicalProfessional

class MedicalProfessionalForm(forms.ModelForm):
    class Meta:
        model = MedicalProfessional
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'occupation',
            'license_number',
            'county',
            'address',
            'status',
            'bio',
            'avatar',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'John',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Doe',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@clinic.com',
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '07XXXXXXXX',
                'class': 'form-control',
            }),
            'occupation': forms.Select(attrs={'class': 'form-select'}),
            'license_number': forms.TextInput(attrs={
                'placeholder': 'e.g., KMPDB123456',
                'class': 'form-control',
            }),
            'county': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={
                'placeholder': 'e.g., Mombasa Road, Block A',
                'class': 'form-control',
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Professional background, education, certifications...',
                'rows': 4,
                'class': 'form-control',
            }),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Surname',
            'email': 'Work Email',
            'phone': 'Mobile Number',
            'occupation': 'Specialization',
            'license_number': 'Medical License Number',
            'county': 'County of Practice',
            'address': 'Clinic Address',
            'status': 'Employment Status',
            'bio': 'Professional Biography',
            'avatar': 'Profile Photo',
        }

# 🔐 User Registration Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email address',
        'class': 'form-control'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# 🔑 User Login Form (optional if customizing)
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))
# Note: The LoginForm is optional if you want to customize the default Django login form.
# You can use the default AuthenticationForm provided by Django if no customization is needed.  