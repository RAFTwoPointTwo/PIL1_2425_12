from django.contrib.auth import login , get_user_model , authenticate
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect , get_object_or_404
from django.db import models
from django.http import JsonResponse
from .models import Trajet,CustomUser
<<<<<<< HEAD
from .models import Trajet
from django.contrib import messages
from .models import Message
from .forms import MessageForm
=======

from .models import Trajet
from django.contrib import messages
>>>>>>> cbaaf95 (Mot de passe oublié)
import json


@login_required
def principale(request):
    return render(request, 'principale.html',{'utilisateurs': CustomUser.objects.all()[:3]})

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compte_cree')
    else:
        form = CustomUserForm()

    return render(request, 'register.html', {'form': form})


def created_account(request):
    return render(request , "compte_cree.html")

@login_required
def profil(request):
    profile = request.user.profile
    return render(request, 'profil.html', {'profile': profile})




User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('principale')
        else:
            messages.error(request, "Email ou mot de passe incorrect.")

    return render(request, 'login.html')


class CustomLogoutView(LogoutView):
    next_page = '/login/'


'''@login_required'''
def chat_room(request, room_name):
    return render(request, 'chat_room.html', {'room_name': room_name})

def matching_page(request):
    return render(request, 'matching_page.html')

from django.shortcuts import render


def enregistrer_trajet(request):
    if request.method == "POST":
        data = json.loads(request.body)
        trajet = Trajet.objects.create(
            start_lat=data.get('start_lat'),
            start_lng=data.get('start_lng'),
            
        )
        trajet.save()
        return JsonResponse({'message': "Trajet enregistré avec succès !"})
    return JsonResponse({'error': "Méthode non autorisée"}, status=405)


@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TrajetForm

@login_required
def choisir_trajet(request):
    message = None
    if request.method == 'POST':
        form = TrajetForm(request.POST)
        if form.is_valid():
            trajet = form.save(commit=False)
            trajet.user = request.user
            trajet.save()
            message = "Trajet enregistré avec succès !"
            form = TrajetForm()  # Réinitialise le formulaire après soumission
    else:
        form = TrajetForm()
    
    return render(request, 'matching_page', {
        'form': form,
        'message': message
    })


