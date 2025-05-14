from django import forms
from .models import Attendance
from datetime import date

class AttendanceForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        initial=date.today
    )
    status = forms.ChoiceField(
        choices=Attendance.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Attendance
        fields = ['date', 'status']

    def clean_date(self):
        attendance_date = self.cleaned_data['date']
        today = date.today()
        if attendance_date > today:
            raise forms.ValidationError("You cannot mark attendance for future dates!")
        return attendance_date