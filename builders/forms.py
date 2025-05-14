from django import forms
from builders.models import Builder, BuilderCompany
from datetime import date

class BuilderCompanyForm(forms.ModelForm):
    registration_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        initial=date.today
    )

    class Meta:
        model = BuilderCompany
        fields = ['name', 'license_number', 'registration_date', 'address', 
                 'phone', 'email', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'})
        }

class BuilderForm(forms.ModelForm):
    class Meta:
        model = Builder
        fields = ['company', 'designation', 'experience_years', 'specialization', 
                 'company_name', 'contact_number']