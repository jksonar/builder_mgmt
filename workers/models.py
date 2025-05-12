from django.db import models
from projects.models import Project

class Worker(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    assigned_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    contact = models.CharField(max_length=20)