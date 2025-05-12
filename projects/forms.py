from django import forms
from projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['builder', 'name', 'location', 'start_date', 'end_date', 'budget']