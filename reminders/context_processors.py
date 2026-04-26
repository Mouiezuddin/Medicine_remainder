from .models import Reminder
from django.utils import timezone
from django.db import models

def today_reminders_count(request):
    if request.user.is_authenticated:
        now = timezone.now()
        today = now.date()
        # Reminders with today's date OR reminders with no specific date (daily)
        reminders = Reminder.objects.filter(
            medicine__user=request.user, 
            is_active=True
        ).filter(
            models.Q(date=today) | models.Q(date__isnull=True)
        ).select_related('medicine').order_by('time')
        
        return {
            'active_reminders_count': reminders.count(),
            'today_reminders': reminders
        }
    return {'active_reminders_count': 0, 'today_reminders': []}
