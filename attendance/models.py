from django.db import models
# from workers.models import Worker
from django.conf import settings

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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)