from django import forms
from builders.models import Builder

class BuilderForm(forms.ModelForm):
    class Meta:
        model = Builder
        fields = ['company_name', 'contact_number']