from django import forms
from .models import Reminder
from medicines.models import Medicine

class ReminderForm(forms.ModelForm):
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
