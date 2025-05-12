from django.shortcuts import render, redirect
from attendance.forms import AttendanceForm
from attendance.models import Attendance

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})


def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'records': records})
