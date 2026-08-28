from django import forms
from myApp.models import *
from django.contrib.auth.forms import UserCreationForm

class registerForm(UserCreationForm):
    class Meta:
        model = customAuth
        fields = ['username', 'email', 'password1', 'password2']


