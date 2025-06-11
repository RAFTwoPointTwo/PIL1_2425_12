from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=15 , unique=True)
    Status = [
        ('passager' , 'Passager'),
        ('conducteur' , 'Conducteur')
    ]
    role = models.CharField(max_length=10 , choices=Status , default='passager')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'phone']

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    photo = models.ImageField("Photo" , upload_to='profiles/' , blank=True , null=True)
    start_point = models.CharField("Point de départ" , max_length=255 , blank=False)
    start_date = models.TimeField("Heure de départ" , blank=False , null=False)
    arrival_date = models.TimeField("Heure d'arrivée" , blank=False , null=False)
    vehicule_marque = models.CharField("Marque de votre véhicule" , max_length=50 , blank=True)
    vehicule_model = models.CharField("Modèle de votre véhicule" , max_length=50 , blank=True)
    vehicule_place = models.PositiveIntegerField("PLaces disponibles dans votre véhicule" , blank=True , null=True)
    def __str__(self):
        return f"Profil de {self.user.username}"