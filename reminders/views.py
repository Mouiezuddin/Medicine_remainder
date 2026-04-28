from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reminder
from medicines.models import Medicine
from .forms import ReminderForm

@login_required
def reminder_list(request):
    date_filter = request.GET.get('date')
    reminders = Reminder.objects.filter(medicine__user=request.user)
    
    if date_filter:
        reminders = reminders.filter(date=date_filter)
        
    return render(request, 'reminders/list.html', {
        'reminders': reminders,
        'selected_date': date_filter
    })

@login_required
def reminder_add(request):
    form = ReminderForm(user=request.user, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Check if user wants to add a new medicine
        if form.cleaned_data.get('add_new_medicine'):
            # Create new medicine
            new_medicine = Medicine.objects.create(
                user=request.user,
                name=form.cleaned_data['new_medicine_name'],
                category=form.cleaned_data.get('new_medicine_category', ''),
                dosage=form.cleaned_data['new_medicine_dosage'],
                quantity=form.cleaned_data.get('new_medicine_quantity', 0)
            )
            # Create reminder with the new medicine
            reminder = form.save(commit=False)
            reminder.medicine = new_medicine
            reminder.save()
            messages.success(request, f'New medicine "{new_medicine.name}" added and reminder set!')
        else:
            # Save reminder with existing medicine
            form.save()
            messages.success(request, 'Reminder set!')
        return redirect('reminder_list')
    return render(request, 'reminders/form.html', {'form': form, 'title': 'Add Reminder'})

@login_required
def reminder_edit(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, medicine__user=request.user)
    form = ReminderForm(user=request.user, data=request.POST or None, instance=reminder)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Reminder updated!')
        return redirect('reminder_list')
    return render(request, 'reminders/form.html', {'form': form, 'title': 'Edit Reminder'})

@login_required
def reminder_delete(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, medicine__user=request.user)
    if request.method == 'POST':
        reminder.delete()
        messages.success(request, 'Reminder deleted!')
        return redirect('reminder_list')
    return render(request, 'reminders/confirm_delete.html', {'reminder': reminder})

@login_required
def reminder_toggle(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, medicine__user=request.user)
    reminder.is_active = not reminder.is_active
    reminder.save()
    return redirect('reminder_list')
