from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=15 , unique=True)
    Status = [
        ('passager' , 'Passager'),
        ('conducteur' , 'Conducteur')
    ]
    role = models.CharField(max_length=10 , unique=True , choices=Status , default='passager')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'phone']

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/' , blank=True , null=True)
    start_point = models.CharField(max_length=255 , blank=True)
    start_date = models.TimeField(blank=True , null=True)
    arrival_date = models.TimeField(blank=True , null=True)
    vehicule_marque = models.CharField(max_length=50 , blank=True)
    vehicule_model = models.CharField(max_length=50 , blank=True)
    vehicule_place = models.PositiveIntegerField(blank=True , null=True)

    def __str__(self):
        return f"Profil de {self.user.email}"