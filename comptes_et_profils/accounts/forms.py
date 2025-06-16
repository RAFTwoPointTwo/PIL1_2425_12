from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import Message,CustomUser,Matching



'''from .models import Message'''


'''class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(required=True, label='Nom')
    first_name = forms.CharField(required=True, label='Prénom')
    username = forms.CharField(required=True, label="Nom d'utilisateur")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1' , 'password2' , 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control w-50'})
            field.label_suffix = ''


class ProfileForm(forms.ModelForm):
    start_date = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )
    arrival_date = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )

    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control w-50'})


class ProfileUpdateForm(forms.ModelForm):
    start_date = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )
    arrival_date = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )

    class Meta:
        model = ProfileUpdate
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control w-50'})


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email" , widget=forms.EmailInput(attrs={'autofocus': True}))'''
'''password = forms.CharField(label = "Mot de passe" , widget=forms.PasswordInput)'''


class CustomLoginForm(forms.Form):
    """Formulaire de connexion personnalisé."""
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)



class CustomUserForm(forms.ModelForm):
    '''username = forms.CharField(max_length=150, label="Nom d'utilisateur",
                               error_messages={})
    password = forms.CharField(widget=forms.PasswordInput)'''
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
        max_length=50,
        error_messages={
        }
    )

    password = forms.CharField(
        label="Mot de passe",
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

    arrival_point = forms.CharField(
        label="Point d'arrivée",
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
        fields = ['nom', 'prenom', 'username', 'password', 'email', 'numero_de_telephone', 'role' , 'start_point' , 'arrival_point' , 'start_date' , 'arrival_date' , 'vehicule_marque' , 'vehicule_model' , 'vehicule_place']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            if 'form-control' not in existing_classes:
                field.widget.attrs['class'] = (existing_classes + ' form-control w-50').strip()
            if field_name == 'vehicule_marque':
                field.widget.attrs['placeholder'] = "Reseignez ce champ uniquement si vous êtes un conducteur"
            elif field_name == 'vehicule_model':
                field.widget.attrs['placeholder'] = "Renseignez ce champ uniquement si vous êtes un conducteur"
            elif field_name == 'vehicule_place':
                field.widget.attrs['placeholder'] = "Renseignez ce champ uniquement si vous êtes un conducteur"

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            return user




            #Forms



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'recipient': forms.Select(attrs={'class': 'form-control'}),
        }


class MatchingForm(forms.ModelForm):
    class Meta:
        model=Matching
        fields= ['heure_de_depart','date_de_depart']
        heure_de_depart = forms.TimeField(
            label="Heure de départ",
            widget=forms.TimeInput(attrs={'type': 'time'}),
            input_formats=['%H:%M']
        )
       