from django import forms
from issues.models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['project', 'title', 'description', 'reported_by', 'status']