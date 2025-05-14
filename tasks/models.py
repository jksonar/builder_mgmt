from django.db import models
from projects.models import Project
from workers.models import Worker

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name