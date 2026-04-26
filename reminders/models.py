from django.db import models
from medicines.models import Medicine

class Reminder(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='reminders')
    time = models.TimeField()
    date = models.DateField(null=True, blank=True, help_text="Optional: Set a specific date for this reminder")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.name} at {self.time}"

    class Meta:
        ordering = ['time']
