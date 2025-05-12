from django import forms
from workers.models import Worker

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'role', 'assigned_project', 'contact']