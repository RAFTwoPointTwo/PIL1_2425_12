from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser , Profile
from django.contrib.auth import get_user_model

user = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('username' , 'email' , 'phone' , 'role')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']