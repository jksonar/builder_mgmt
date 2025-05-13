from django.db import models
from projects.models import Project

class Site(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField()
    area_size = models.DecimalField(max_digits=10, decimal_places=2)
    site_engineer = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    area_sqft = models.FloatField()