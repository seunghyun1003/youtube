from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            "username": "username",
            "email": "email",
            "password": "password",
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password'] 
        labels = {
            "username": "username",
            "password": "password",
        }