from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from attendance.forms import AttendanceForm
from attendance.models import Attendance

@login_required
def mark_attendance(request):
    attendance_id = request.GET.get('id')
    instance = None
    
    if attendance_id:
        instance = get_object_or_404(Attendance, id=attendance_id, employee=request.user)
    
    if request.method == 'POST':
        form = AttendanceForm(
            request.POST, 
            instance=instance,
            user=request.user,
            instance_id=attendance_id
        )
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.employee = request.user
            attendance.save()
            messages.success(request, 'Attendance marked successfully!')
            return redirect('attendance_list')
    else:
        form = AttendanceForm(
            instance=instance,
            user=request.user,
            instance_id=attendance_id
        )
    
    context = {
        'form': form,
        'is_edit': bool(instance)
    }
    return render(request, 'attendance/mark_attendance.html', {'form': form})

@login_required
def attendance_list(request):
    records = Attendance.objects.filter(employee=request.user).order_by('-date')
    return render(request, 'attendance/attendance_list.html', {'records': records})
