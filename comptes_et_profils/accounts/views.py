from django.contrib.auth import login , authenticate
from .forms import CustomLoginForm , CustomUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect , get_object_or_404
'''from .models import Message'''
from django.db import models
from django.http import JsonResponse
from .models import Trajet
import json



def principale(request):
    return render(request, 'principale.html')


'''def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Récupération manuelle des données
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password1']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            phone = user_form.cleaned_data['phone']
            role = user_form.cleaned_data['role']

            # Création manuelle de l'utilisateur
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                role=role
            )
            # Création du profil
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('principale')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })'''


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


'''@login_required
def profil_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:

        form = ProfileForm(instance=profile)
        return render(request, 'profil_edit.html', {'form': form})'''




'''@login_required
def dashboard(request):
    return render(request, 'dashboard.html')'''


'''class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentification_form = CustomLoginForm'''

def CustomLoginView(request):
    form = CustomLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('principale')
        else:
            form.add_error(None, "Email ou mot de passe incorrect.")
    return render(request, 'login.html', {'form': form})

class CustomLogoutView(LogoutView):
    next_page = '/login/'


# Vue messagerie
#vues


'''@login_required'''
'''def chat(request, recipient_email=None):
    recipient = None
    if recipient_email:
        try:
            recipient = User.objects.get(email=recipient_email)
        except User.DoesNotExist:
            pass

    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('chat', recipient_email=recipient.email)
    else:
        form = MessageForm(user=request.user)
        if recipient:
            form.fields['receiver'].initial = recipient

    # Récupération des conversations

    conversations = Message.objects.filter(
        models.Q(sender=request.user) | models.Q(receiver=request.user)
    ).order_by('timestamp')

    return render(request, 'chat/chat.html', {
        'form': form,
        'conversations': conversations,
        'active_recipient': recipient,
    })'''


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
            end_lat=data.get('end_lat'),
            end_lng=data.get('end_lng')
        )
        return JsonResponse({'message': "Trajet enregistré avec succès !"})
    return JsonResponse({'error': "Méthode non autorisée"}, status=405)
