from django.db import models
from projects.models import Project

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('Available', 'Available'), ('In Use', 'In Use'), ('Under Maintenance', 'Under Maintenance')])
    assigned_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
