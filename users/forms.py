from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password', 'phone_number', 'address']
        widgets = {
            'password': forms.PasswordInput()
        }