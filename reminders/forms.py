from django import forms
from .models import Reminder
from medicines.models import Medicine

class ReminderForm(forms.ModelForm):
    # Option to add new medicine inline
    add_new_medicine = forms.BooleanField(
        required=False, 
        label="Add new medicine",
        widget=forms.CheckboxInput(attrs={'class': 'glass-checkbox'})
    )
    
    # New medicine fields (only shown when add_new_medicine is checked)
    new_medicine_name = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'glass-input', 
            'placeholder': 'e.g. Paracetamol'
        }),
        label="Medicine Name"
    )
    new_medicine_category = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'glass-input', 
            'placeholder': 'e.g. Painkiller'
        }),
        label="Category"
    )
    new_medicine_dosage = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'glass-input', 
            'placeholder': 'e.g. 500mg'
        }),
        label="Dosage"
    )
    new_medicine_quantity = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'glass-input', 
            'placeholder': 'e.g. 30'
        }),
        label="Quantity"
    )

    class Meta:
        model = Reminder
        fields = ['medicine', 'date', 'time', 'is_active']
        widgets = {
            'medicine': forms.Select(attrs={'class': 'glass-input'}),
            'date': forms.DateInput(attrs={'class': 'glass-input', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'glass-input', 'type': 'time'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'glass-checkbox'}),
        }

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['medicine'].queryset = Medicine.objects.filter(user=user)
            # Add empty option to encourage adding new medicine if no medicines exist
            if not Medicine.objects.filter(user=user).exists():
                self.fields['medicine'].empty_label = "No medicines available - check 'Add new medicine' below"
                self.fields['add_new_medicine'].initial = True
        
        # Make medicine field not required initially - we'll validate in clean()
        self.fields['medicine'].required = False

    def clean(self):
        cleaned_data = super().clean()
        add_new_medicine = cleaned_data.get('add_new_medicine')
        medicine = cleaned_data.get('medicine')
        
        if add_new_medicine:
            # Validate new medicine fields
            new_name = cleaned_data.get('new_medicine_name')
            new_dosage = cleaned_data.get('new_medicine_dosage')
            
            if not new_name:
                raise forms.ValidationError("Medicine name is required when adding a new medicine.")
            if not new_dosage:
                raise forms.ValidationError("Medicine dosage is required when adding a new medicine.")
            
            # Clear medicine field error since we're adding a new one
            if 'medicine' in self.errors:
                del self.errors['medicine']
                
        elif not medicine and not add_new_medicine:
            raise forms.ValidationError("Please select a medicine or choose to add a new one.")
            
        return cleaned_data
