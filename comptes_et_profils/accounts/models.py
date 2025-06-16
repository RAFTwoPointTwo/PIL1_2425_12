from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    numero_de_telephone = models.CharField(max_length=10 , unique=True , null=False)
    TYPE_CHOIX = [
        ('passager', 'Passager'),
        ('conducteur', 'Conducteur'),
    ]
    role = models.CharField(max_length=12, choices=TYPE_CHOIX, default='passager')
    start_point = models.CharField("Point de départ habituel", max_length=50, blank=False)
    start_date = models.TimeField("Heure de départ", blank=False, null=False ,default=timezone.now)
    arrival_date = models.TimeField("Heure d'arrivée", blank=False, null=False , default=timezone.now)
    vehicule_marque = models.CharField("Marque de votre véhicule", max_length=50, blank=True)
    vehicule_model = models.CharField("Modèle de votre véhicule", max_length=50, blank=True)
    vehicule_place = models.PositiveIntegerField("PLaces disponibles dans votre véhicule", blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.email}"

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


    def __str__(self):
        return f"De {self.sender} à {self.recipient} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"
    
class Discussion(models.Model):
    ancients_messages = models.ManyToManyField(Message, related_name='discussions')
    nouveau_message =models.TextField()


class Trajet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='voyager' )
    start_lat = models.FloatField()
    start_lng = models.FloatField()
    heure_depart = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trajet de {self.user.username} à {self.heure_depart}"



