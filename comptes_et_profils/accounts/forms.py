from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Message,CustomUser
from .models import Trajet

class CustomUserForm(forms.ModelForm):
    start_date = forms.TimeField(
        label="Heure de départ habituelle",
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )
    arrival_date = forms.TimeField(
        label="Heure d'arrivée",
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )
    nom = forms.CharField(
        label="Nom",
        max_length=50,
        error_messages={
            'invalid': 'Le nom ne peut pas dépasser 50 caracteres.'
        }
    )

    prenom = forms.CharField(
        label="Prénoms",
        max_length=50,
        error_messages={
            'invalid': 'Les prénoms ne peuvent pas dépasser 50 caracteres.'
        }
    )

    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=150,
        error_messages={
        }
    )

    password = forms.CharField(
        label="Mot de passe",
        min_length=8,
        widget=forms.PasswordInput,
        error_messages={
        }
    )

    email = forms.EmailField(
        label="Email",
        max_length=254,
        error_messages={
            'invalid': 'Veuillez entrer une adresse e-mail valide.'
        }
    )
    role = forms.ChoiceField(
        label="Role",
        choices=[
            ('passager', 'Passager'),
            ('conducteur', 'Conducteur'),
        ]
    )

    numero_de_telephone = forms.CharField(
        label="Numero de telephone",
        error_messages={
            'invalid': 'Veuillez entrer un numero de telephone valide.'
        }
    )

    start_point = forms.CharField(
        label="Point de départ habituel",
        error_messages={
            'invalid': 'Les informations de ce champ ne peuvent pas dépasser 50 caracteres.'
        }
    )

    vehicule_marque = forms.CharField(
        label="Marque de votre véhicule",
        required=False,
        error_messages={
            'invalid': 'Les informations de ce champ ne peuvent pas dépasser 50 caracteres.'
        }
    )
    vehicule_model = forms.CharField(
        label="Modèle de votre véhicule",
        required=False,
        error_messages={
            'invalid': 'Les informations de ce champ ne peuvent pas dépasser 50 caracteres.'
        }
    )
    vehicule_place = forms.IntegerField(
        label="Marque de votre véhicule",
        required=False,
        error_messages={
            'invalid': 'Les informations de ce champ ne peuvent pas dépasser 50 caracteres.'
        }
    )

    class Meta:
        model = CustomUser
        fields = ['nom', 'prenom', 'username', 'password', 'email', 'numero_de_telephone', 'role' , 'start_point' , 'start_date' , 'arrival_date' , 'vehicule_marque' , 'vehicule_model' , 'vehicule_place']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            if 'form-control' not in existing_classes:
                field.widget.attrs['class'] = (existing_classes + ' form-control w-100').strip()
            if field_name == 'vehicule_marque':
                field.widget.attrs['placeholder'] = "Reseignez ce champ uniquement si vous êtes un conducteur"
            elif field_name == 'vehicule_model':
                field.widget.attrs['placeholder'] = "Renseignez ce champ uniquement si vous êtes un conducteur"
            elif field_name == 'vehicule_place':
                field.widget.attrs['placeholder'] = "Renseignez ce champ uniquement si vous êtes un conducteur"

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nom', 'prenom', 'email', 'numero_de_telephone', 'role' , 'start_point' , 'start_date' , 'arrival_date' , 'vehicule_marque' , 'vehicule_model' , 'vehicule_place']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            if 'form-control' not in existing_classes:
                field.widget.attrs['class'] = (existing_classes + ' form-control w-100').strip()
            if field_name == 'vehicule_marque':
                field.widget.attrs['placeholder'] = "Reseignez ce champ uniquement si vous êtes un conducteur"
            elif field_name == 'vehicule_model':
                field.widget.attrs['placeholder'] = "Renseignez ce champ uniquement si vous êtes un conducteur"
            elif field_name == 'vehicule_place':
                field.widget.attrs['placeholder'] = "Renseignez ce champ uniquement si vous êtes un conducteur"



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'recipient': forms.Select(attrs={'class': 'form-control'}),
        }

class TrajetForm(forms.ModelForm):
        date_depart = forms.DateField(
            label="Date de départ",
            widget=forms.DateInput(attrs={'type': 'date'}),
            input_formats=['%Y-%m-%d'],
            error_messages={
                'invalid': 'Veuillez entrer une date valide au format AAAA-MM-JJ.'
            }
        )
  
        point_depart = forms.CharField(
            label="Point de départ",
            max_length=100,
            error_messages={
                'invalid': 'Le point de départ ne peut pas dépasser 100 caractères.'
            }
        )
        heure_depart = forms.TimeField(
            label="Heure de départ",
            widget=forms.TimeInput(attrs={'type': 'time'}),
            input_formats=['%H:%M'],
            error_messages={
                'invalid': 'Veuillez entrer une heure valide au format HH:MM.'
            }
        )
        class Meta:
          model = Trajet
          fields = ['point_depart','date_depart', 'heure_depart']