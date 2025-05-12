from django.db import models
from workers.models import Worker

class Attendance(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)