from django.db import models
from projects.models import Project
from suppliers.models import Supplier

class Material(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)