from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'glass-input', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'glass-input', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'glass-input', 'placeholder': 'Confirm Password'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'glass-input'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'glass-input', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'glass-input', 'placeholder': 'Password'})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone_number', 'date_of_birth', 'address', 
            'emergency_contact_name', 'emergency_contact_phone',
            'medical_conditions', 'doctor_name', 'doctor_phone',
            'insurance_provider', 'insurance_policy_number'
        ]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': '+1 (555) 123-4567'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'glass-input', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'glass-input', 'rows': 3, 'placeholder': '123 Main St, City, State, ZIP'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'John Doe'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': '+1 (555) 987-6543'}),
            'medical_conditions': forms.Textarea(attrs={'class': 'glass-input', 'rows': 3, 'placeholder': 'Any allergies, chronic conditions, or medical notes...'}),
            'doctor_name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Dr. Smith'}),
            'doctor_phone': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': '+1 (555) 111-2222'}),
            'insurance_provider': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Blue Cross Blue Shield'}),
            'insurance_policy_number': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'ABC123456789'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'glass-input'}),
            'last_name': forms.TextInput(attrs={'class': 'glass-input'}),
            'email': forms.EmailInput(attrs={'class': 'glass-input'}),
        }