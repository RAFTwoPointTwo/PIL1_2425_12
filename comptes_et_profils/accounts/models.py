from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


''''class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email :
            raise ValueError("L'email est requis")   
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user



    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)  

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)'''

'''class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=15 , unique=True)
    password=models.CharField(max_length=25,unique=True)

    Status = [
        ('passager' , 'Passager'),
        ('conducteur' , 'Conducteur')
    ]
    nom = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

   # objects = CustomUserManager()  #  important !

    role = models.CharField(max_length=10 , choices=Status , default='passager')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'phone','password' ]

    def __str__(self):
        return self.email'''


'''class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField("Photo", upload_to='profiles/', blank=True, null=True)
    phone = models.CharField("Numero de téléphone", max_length=15, unique=True)
    start_point = models.CharField("Point de départ", max_length=255, blank=False)
    start_date = models.TimeField("Heure de départ", blank=False, null=False ,default=timezone.now)
    arrival_date = models.TimeField("Heure d'arrivée", blank=False, null=False , default=timezone.now)
    Status = [
        ('passager', 'Passager'),
        ('conducteur', 'Conducteur')
    ]
    role = models.CharField("Statut", max_length=10, choices=Status, default='passager')
    vehicule_marque = models.CharField("Marque de votre véhicule", max_length=50, blank=True)
    vehicule_model = models.CharField("Modèle de votre véhicule", max_length=50, blank=True)
    vehicule_place = models.PositiveIntegerField("PLaces disponibles dans votre véhicule", blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.user.username}"


class ProfileUpdate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField("Photo", upload_to='profiles/', blank=True, null=True)
    phone = models.CharField("Numero de téléphone", max_length=15, unique=True)
    start_point = models.CharField("Point de départ", max_length=255, blank=False)
    start_date = models.TimeField("Heure de départ", blank=False, null=False)
    arrival_date = models.TimeField("Heure d'arrivée", blank=False, null=False)
    Status = [
        ('passager', 'Passager'),
        ('conducteur', 'Conducteur')
    ]
    role = models.CharField("Statut", max_length=10, choices=Status, default='passager')
    vehicule_marque = models.CharField("Marque de votre véhicule", max_length=50, blank=True)
    vehicule_model = models.CharField("Modèle de votre véhicule", max_length=50, blank=True)
    vehicule_place = models.PositiveIntegerField("PLaces disponibles dans votre véhicule", blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.user.username}"'''

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
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
    arrival_point = models.CharField("Point de destination" , max_length=50, blank=False)
    start_date = models.TimeField("Heure de départ", blank=False, null=False ,default=timezone.now)
    arrival_date = models.TimeField("Heure d'arrivée", blank=False, null=False , default=timezone.now)
    vehicule_marque = models.CharField("Marque de votre véhicule", max_length=50, blank=True)
    vehicule_model = models.CharField("Modèle de votre véhicule", max_length=50, blank=True)
    vehicule_place = models.PositiveIntegerField("PLaces disponibles dans votre véhicule", blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.username}"

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')


#Modèles messagerie
#models
#models

'''class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def _str_(self):
        return f"From {self.sender.email} to {self.receiver.email}: {self.content[:20]}..."'''


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


    def __str__(self):
        return f"De {self.sender} à {self.recipient} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"
    





class Trajet(models.Model):
   # paasger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_lat = models.FloatField()
    start_lng = models.FloatField()
    end_lat = models.FloatField()
    end_lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trajet du {self.created_at.strftime('%Y-%m-%d %H:%M')}"


'''class Matching(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    heure_de_depart = models.TimeField()
    date_de_depart = models.DateField()

    def __str__(self):
        return f"Matching pour {self.user.username} le {self.matched_at.strftime('%Y-%m-%d %H:%M')}"'''