from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicine
from .forms import MedicineForm

@login_required
def medicine_list(request):
    medicines = Medicine.objects.filter(user=request.user)
    return render(request, 'medicines/list.html', {'medicines': medicines})

@login_required
def medicine_add(request):
    form = MedicineForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        med = form.save(commit=False)
        med.user = request.user
        med.save()
        messages.success(request, 'Medicine added!')
        return redirect('medicine_list')
    return render(request, 'medicines/form.html', {'form': form, 'title': 'Add Medicine'})

@login_required
def medicine_edit(request, pk):
    med = get_object_or_404(Medicine, pk=pk, user=request.user)
    form = MedicineForm(request.POST or None, instance=med)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Medicine updated!')
        return redirect('medicine_list')
    return render(request, 'medicines/form.html', {'form': form, 'title': 'Edit Medicine'})

@login_required
def medicine_delete(request, pk):
    med = get_object_or_404(Medicine, pk=pk, user=request.user)
    if request.method == 'POST':
        med.delete()
        messages.success(request, 'Medicine deleted!')
        return redirect('medicine_list')
    return render(request, 'medicines/confirm_delete.html', {'medicine': med})
