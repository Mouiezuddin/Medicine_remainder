from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reminders.models import Reminder

@login_required
def dashboard(request):
    active_reminders = Reminder.objects.filter(
        medicine__user=request.user,
        is_active=True
    ).select_related('medicine')
    return render(request, 'dashboard/index.html', {'reminders': active_reminders})

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')
