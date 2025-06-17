from django.contrib.auth import login , get_user_model , authenticate
from .forms import CustomUserForm , CustomUserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Trajet,CustomUser
from django.contrib import messages
from .models import Message , Profile
from .forms import MessageForm , TrajetForm
import json
import folium
from geopy.geocoders import Nominatim


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
    return render(request, 'profile.html', {'profile': profile})

@login_required
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            print("Données validées :", form.cleaned_data)
            form.save()
            messages.success(request, "Vos informations ont été mises à jour.")
            return redirect('profile')
    else:
        form = CustomUserUpdateForm(instance=user)
    return render(request, 'profile_update.html', {'form': form})



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


def map_page(request):
    user = request.user
    try:
        profil = user.profile
        print(f"profil {profil}")
        lieu_depart = user.start_point
        print(f"lieu de depart : {lieu_depart}")
    except:
        lieu_depart = None
        print(f"lieu de depart {lieu_depart}")

    if not lieu_depart:
        return render(request, 'map_page.html', {'message': "Aucun lieu de départ défini."})

    geolocator = Nominatim(user_agent="Map_profile")
    start_location = geolocator.geocode(lieu_depart)
    uac_location = geolocator.geocode("Université d'Abomey-Calavi, Bénin")

    if not start_location or not uac_location:
        return render(request, 'map_page.html', {'message': "Impossible de localiser les lieux."})

    m = folium.Map(
        location=[(start_location.latitude + uac_location.latitude) / 2,
                  (start_location.longitude + uac_location.longitude) / 2],
        zoom_start=11
    )

    folium.Marker(
        [start_location.latitude, start_location.longitude],
        popup="Départ : " + lieu_depart,
        tooltip=f"{lieu_depart}",
        icon=folium.Icon(color='blue')
    ).add_to(m)

    folium.Marker(
        [uac_location.latitude, uac_location.longitude],
        popup="Université d'Abomey-Calavi (UAC)",
        tooltip="UAC",
        icon=folium.Icon(color='red')
    ).add_to(m)

    folium.PolyLine(
        [(start_location.latitude, start_location.longitude),
         (uac_location.latitude, uac_location.longitude)],
        color='green',
        weight=5,
        opacity=0.8
    ).add_to(m)

    map_html = m._repr_html_()
    return render(request, 'map_page.html', {'map': map_html})



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