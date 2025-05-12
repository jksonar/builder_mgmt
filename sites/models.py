from django.db import models
from projects.models import Project

class Site(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    area_sqft = models.FloatField()