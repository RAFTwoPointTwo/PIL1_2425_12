from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager,PermissionsMixin,User



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
    




class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    photo = models.ImageField("Photo" , upload_to='profiles/' , blank=True , null=True)
    phone = models.CharField("Numero de téléphone",  max_length=15 , unique=True)
    start_point = models.CharField("Point de départ" , max_length=255 , blank=False)
    start_date = models.PositiveIntegerField("Heure de départ" , blank=False , null=False)
    arrival_date = models.PositiveIntegerField("Heure d'arrivée" , blank=False , null=False)
    Status = [
        ('passager' , 'Passager'),
        ('conducteur' , 'Conducteur')
    ]
    role = models.CharField( "Statut", max_length=10 , choices=Status , default='passager')
    vehicule_marque = models.CharField("Marque de votre véhicule" , max_length=50 , blank=True)
    vehicule_model = models.CharField("Modèle de votre véhicule" , max_length=50 , blank=True)
    vehicule_place = models.PositiveIntegerField("PLaces disponibles dans votre véhicule" , blank=True , null=True)
    
    def __str__(self):
        return f"Profil de {self.user.username}"
    


class ProfileUpdate(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    photo = models.ImageField("Photo" , upload_to='profiles/' , blank=True , null=True)
    phone = models.CharField("Numero de téléphone",  max_length=15 , unique=True)
    start_point = models.CharField("Point de départ" , max_length=255 , blank=False)
    start_date = models.TimeField("Heure de départ" , blank=False , null=False)
    arrival_date = models.TimeField("Heure d'arrivée" , blank=False , null=False)
    Status = [
        ('passager' , 'Passager'),
        ('conducteur' , 'Conducteur')
    ]
    role = models.CharField( "Statut", max_length=10 , choices=Status , default='passager')
    vehicule_marque = models.CharField("Marque de votre véhicule" , max_length=50 , blank=True)
    vehicule_model = models.CharField("Modèle de votre véhicule" , max_length=50 , blank=True)
    vehicule_place = models.PositiveIntegerField("PLaces disponibles dans votre véhicule" , blank=True , null=True)
    def __str__(self):
        return f"Profil de {self.user.username}"
        
    

