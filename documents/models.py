from django.db import models
from projects.models import Project

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    type = models.CharField(max_length=50)