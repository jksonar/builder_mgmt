from django.db import models
from projects.models import Project

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    assigned_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)