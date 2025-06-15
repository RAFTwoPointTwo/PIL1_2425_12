from django.contrib.auth import login , authenticate
from .forms import CustomLoginForm , CustomUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect , get_object_or_404
from django.db import models
from django.http import JsonResponse
from .models import Trajet
import json


@login_required
def principale(request):
    return render(request, 'principale.html')

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




'''class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentification_form = CustomLoginForm'''

'''def CustomLoginView(request):
    form = CustomLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('principale')
        else:
            form.add_error(None, "Email ou mot de passe incorrect.")
    return render(request, 'login.html', {'form': form})'''

'''class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm
    redirect_authenticated_user = True'''


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm
    redirect_authenticated_user = True
    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Email ou mot de passe incorrect.")
            return self.form_invalid(form)


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
            end_lat=data.get('end_lat'),
            end_lng=data.get('end_lng')
        )
        return JsonResponse({'message': "Trajet enregistré avec succès !"})
    return JsonResponse({'error': "Méthode non autorisée"}, status=405)
