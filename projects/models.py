from django.db import models
from builders.models import BuilderCompany

class Project(models.Model):
    name = models.CharField(max_length=200)
    builder = models.ForeignKey(BuilderCompany, on_delete=models.CASCADE)
    location = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50)
    description = models.TextField()