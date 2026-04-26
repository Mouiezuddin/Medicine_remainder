from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Antibiotic, Painkiller")
    dosage = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0, help_text="Number of tablets/pills available")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.dosage}) - {self.quantity} tablets"

    class Meta:
        ordering = ['-created_at']
