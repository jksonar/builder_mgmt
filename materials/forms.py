from django import forms
from materials.models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'quantity', 'unit', 'project', 'supplier']