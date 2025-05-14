from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from attendance.forms import AttendanceForm
from attendance.models import Attendance

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.employee = request.user
            attendance.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})

@login_required
def attendance_list(request):
    records = Attendance.objects.filter(employee=request.user)
    return render(request, 'attendance/attendance_list.html', {'records': records})
