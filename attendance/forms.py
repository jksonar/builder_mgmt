from django import forms
from .models import Attendance
from datetime import date, datetime

class AttendanceForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        initial=date.today
    )
    time_in = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control',
            'step': '300',  # 5-minute intervals
            'min': '06:00',  # Earliest allowed time
            'max': '22:00',  # Latest allowed time
            'onchange': 'validateTimes()'
        })
    )
    time_out = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control',
            'step': '300',  # 5-minute intervals
            'min': '06:00',  # Earliest allowed time
            'max': '22:00',  # Latest allowed time
            'onchange': 'validateTimes()'
        })
    )
    status = forms.ChoiceField(
        choices=Attendance.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Attendance
        fields = ['date', 'time_in', 'time_out', 'status']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.instance_id = kwargs.pop('instance_id', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        time_in = cleaned_data.get('time_in')
        time_out = cleaned_data.get('time_out')
        
        if time_in and time_out and time_in > time_out:
            raise forms.ValidationError("Time out must be after time in")
        
        return cleaned_data

    def clean_date(self):
        attendance_date = self.cleaned_data['date']
        today = date.today()
        
        if attendance_date > today:
            raise forms.ValidationError("You cannot mark attendance for future dates!")
        
        existing_attendance = Attendance.objects.filter(
            employee=self.user,
            date=attendance_date
        )
        
        if self.instance_id:
            existing_attendance = existing_attendance.exclude(id=self.instance_id)
            
        if existing_attendance.exists():
            raise forms.ValidationError("Attendance for this date has already been marked!")
            
        return attendance_date