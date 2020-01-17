from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from userprofile.models import profile  # import profile model from userprofile

class registration(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
        ]

#extending profile model

class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=[
            'bio',
            'location',
            'birth_date',
            'profile_image',

        ]
# Meta gives us more fields that Already existed in our model
# Meta class  is always used for adding extra fields to User model

