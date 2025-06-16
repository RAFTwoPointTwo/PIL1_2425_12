from geopy.distance import geodesic
from datetime import datetime, date
from .models import Trajet, CustomUser
from .models import Trajet, CustomUser #, Matching
import datetime
import geopy
import time

def matching(request):
    user = request.user

    try:
        mon_trajet = Trajet.objects.filter(user=user).latest('created_at')
    except Trajet.DoesNotExist:
        return []  # Aucun trajet disponible pour l'utilisateur

    # Heure de départ convertie en datetime
    heure_depart = datetime.combine(date.today(), mon_trajet.heure_depart)

    # Tous les trajets sauf ceux du user actuel
    trajets_autres = Trajet.objects.exclude(user=user)

    matches = []
    for trajet in trajets_autres:
        if trajet.user.role == user.role:
            continue  # On veut matcher avec l’autre rôle

        heure_autre = datetime.combine(date.today(), trajet.heure_depart)
        ecart_temps = abs((heure_depart - heure_autre).total_seconds())

        if ecart_temps <= 1800:  # ±30 min
            # Distance entre les points
            coord1 = (mon_trajet.start_lat, mon_trajet.start_lng)
            coord2 = (trajet.start_lat, trajet.start_lng)
            distance = geodesic(coord1, coord2).km

            if distance <= 3:  # Par exemple : rayon de 3km
                matches.append(trajet)

    return matches

passagers_compatibles = []
conducteurs_compatibles = []

def matching(request):
    utilisateur = request.user
    
    # Déterminer si l'utilisateur est un conducteur ou un passager
    if utilisateur.role == "conducteur":
        for trajet in Trajet.objects.all():
            voyageur = trajet.user
            if voyageur.role == "passager" and voyageur.id != utilisateur.id:
                passagers_compatibles.append(voyageur.id)

    elif utilisateur.role == "passager":
        for trajet in Trajet.objects.all():
            conducteur = trajet.user
            if conducteur.role == "conducteur" and conducteur.id != utilisateur.id:
                conducteurs_compatibles.append(conducteur.id)

    return {"passagers_compatibles": passagers_compatibles, "conducteurs_compatibles": conducteurs_compatibles}
