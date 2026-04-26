from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'category', 'dosage', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'e.g. Paracetamol'}),
            'category': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'e.g. Painkiller'}),
            'dosage': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'e.g. 500mg'}),
            'quantity': forms.NumberInput(attrs={'class': 'glass-input', 'placeholder': 'e.g. 30', 'min': '0'}),
        }
