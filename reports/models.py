from django.db import models
from projects.models import Project

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    generated_on = models.DateField(auto_now_add=True)