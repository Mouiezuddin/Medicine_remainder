from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reminders.models import Reminder
from medicines.models import Medicine
from django.db.models import Count

@login_required
def dashboard(request):
    active_reminders = Reminder.objects.filter(
        medicine__user=request.user,
        is_active=True
    ).select_related('medicine')
    
    # Medicine statistics for the user
    total_medicines = Medicine.objects.filter(user=request.user).count()
    low_stock_medicines = Medicine.objects.filter(user=request.user, quantity__lte=5).count()
    categories_count = Medicine.objects.filter(user=request.user).values('category').distinct().count()
    
    context = {
        'reminders': active_reminders,
        'total_medicines': total_medicines,
        'low_stock_medicines': low_stock_medicines,
        'categories_count': categories_count,
    }
    return render(request, 'dashboard/index.html', context)

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')
