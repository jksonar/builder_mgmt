from django.db import models
# from workers.models import Worker
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import datetime, time

# class Attendance(models.Model):
#     worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
#     date = models.DateField()
#     status = models.CharField(max_length=20)
# in attendance/models.py

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('half_day', 'Half Day'),
        ('absent', 'Absent'),
    ]
    
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    class Meta:
        unique_together = ['employee', 'date']
        
    def clean(self):
        if self.time_in and self.time_out and self.time_in > self.time_out:
            raise ValidationError("Time out must be after time in")