from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from datetime import datetime, date
from .models import Trajet, CustomUser,Match



import requests
from datetime import datetime, date
from geopy.geocoders import Nominatim
from .models import Trajet, Match

geolocator = Nominatim(user_agent="matching_app")

# Fonction pour récupérer la distance via OSRM
def get_osrm_distance(coord1, coord2):
    osrm_url = f"http://router.project-osrm.org/route/v1/driving/{coord1[1]},{coord1[0]};{coord2[1]},{coord2[0]}?overview=false"
    response = requests.get(osrm_url)
    
    if response.status_code == 200:
        data = response.json()
        return data["routes"][0]["distance"] / 1000  # Convertir en km
    else:
        print(f"Erreur API OSRM : {response.status_code}")
        return None  # Retourne None si erreur

def matching(request):
    user = request.user

    try:
        mon_trajet = Trajet.objects.filter(user=user).latest('created_at')
    except Trajet.DoesNotExist:
        return []  

    heure_depart = datetime.combine(date.today(), mon_trajet.heure_depart)
    trajets_autres = Trajet.objects.exclude(user=user) 

    matches = []
    for trajet in trajets_autres:
        if trajet.user.role == user.role:
            continue  

        if trajet.date_depart != mon_trajet.date_depart:
            continue  

        heure_autre = datetime.combine(date.today(), trajet.heure_depart)
        ecart_temps = abs((heure_depart - heure_autre).total_seconds())

        if ecart_temps <= 1800:  
            try:
                position1 = geolocator.geocode(mon_trajet.point_depart)
                position2 = geolocator.geocode(trajet.point_depart)
                
                if position1 and position2:
                    coord1 = (position1.latitude, position1.longitude)
                    coord2 = (position2.latitude, position2.longitude)

                    distance = get_osrm_distance(coord1, coord2)  # OSRM au lieu de geodesic
                    if distance is not None and distance <= 6 :
                        match_exist = Match.objects.filter(trajet_1=mon_trajet, trajet_2=trajet).exists()
                        
                        if not match_exist:
                            Match.objects.create(
                                trajet_1=mon_trajet,
                                trajet_2=trajet,
                                user=trajet.user,
                                distance=round(distance, 2),
                                ecart_temps=int(ecart_temps / 60),
                                date_depart=mon_trajet.date_depart
                            )

                        matches.append({
                            'user': trajet.user,
                            'trajet_1': mon_trajet,
                            'trajet_2': trajet,
                            'distance': distance,
                            'ecart_temps': ecart_temps / 60,
                            'date_depart': mon_trajet.date_depart,
                        })

    
                        
            except Exception as e:
                print(f"Erreur lors du calcul de la distance: {e}")    
    def remove_duplicates(matches):
        unique_matches = []
        seen_users = set()  # Stocke les utilisateurs déjà ajoutés
    
        for match in matches:
            user = match['user']  # Utiliser uniquement le champ "user"
        
            if user not in seen_users:
               seen_users.add(user)
               unique_matches.append(match)
    
        return unique_matches

            

    return remove_duplicates(matches) 




