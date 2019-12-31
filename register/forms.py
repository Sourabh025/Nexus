from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class registration(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]
