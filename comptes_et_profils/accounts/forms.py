from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import  Profile ,ProfileUpdate
from django.contrib.auth import get_user_model

user = get_user_model()

'''class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing_classes + ' form-control w-50 container justify-content-center align-items-center h-25').strip()'''

class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(required=True, label='Nom')
    first_name = forms.CharField(required=True , label='Prénom')
    username = forms.CharField(required = True , label = "Nom d'utilisateur")
    

    class Meta:
        model = user
        fields = ('first_name' , 'last_name' , 'username','password' , 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control w-50'})
            field.label_suffix =''

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control w-50'})

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileUpdate
        exclude = ['user']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control w-50'})



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput)                
