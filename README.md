# 🚗 Logisticar – Application de Covoiturage  
**Réalisée avec Django, HTML, CSS, JavaScript et Folium**  
**PIL1_2425_12**

---

## 🎓 Contexte

Chaque année, l’Institut de Formation et de Recherche en Informatique (IFRI) de l’Université d’Abomey-Calavi soumet un défi aux étudiants de la Licence 1.  
Le projet de cette année consistait à créer une **application web de covoiturage** en 2 semaines.

La réalisation de cette plateforme nous a permis de nous former , et appliquer nos connaissances obtenues en **Django**, d’intégrer des composants interactifs en du **JavaScript**, de styliser l’interface avec du **CSS** et du **Bootstrap**, et d’afficher des cartes géographiques avec **Folium**.

---

## 🚙 Logisticar
**Une Application Web Innovante**

---

## 🔑 Fonctionnalités

- **Inscription et Connexion** : Création de compte avec rôle (passager/conducteur), login sécurisé, vérification d’unicité.
- **Récupération de mot de passe** : Système de réinitialisation par email.
- **Profil Utilisateur** : Informations personnelles, habitudes de trajets, infos véhicule si conducteur.
- **Matching intelligent** :  
  Une fois connecté, indiquez votre **point de départ habituel** et vos **horaires de déplacement**.  
  - En tant que **passager**, l’application vous propose des **conducteurs ayant un trajet similaire**.  
  - En tant que **conducteur**, vous recevez des **demandes de passagers** correspondant à votre itinéraire.  
  Le système de **matching** repose sur la **proximité géographique** et la **concordance horaire**, pour favoriser les trajets partagés efficaces, sécurisés et pratiques.
- **Carte interactive** : Affichage dynamique des trajets et positions géographiques avec **Folium**.
- **Modification du profil** : Possibilité de modifier à tout moment ses données.

---

## ⚙️ Technologies utilisées

- **Python 3**  
- **Django**  
- **HTML / CSS / JavaScript**  
- **Bootstrap 5**  
- **Folium**

---

## 🧭 Installation

### 1. Créer et activer un environnement virtuel

#### Sous **Windows** :

```bash
python -m venv mon_env
mon_env\Scripts\activate
```
#### Sous **Linux** :

```bash
python3 -m venv mon_env
source mon_env/bin/activate
```

# 2. Cloner le dépôt

```bash
git clone https://github.com/RAFTwoPointTwo/PIL1_2425_12.git
cd PIL1_2425_12
```

# 3. Installer Django

```bash
pip install django
```

# 4. Configurer la base de données
# SQLite (par défaut) :

```bash
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}
```

# MySQL :

```bash
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': '[Nom de votre base de données]',
    'USER': '[Votre nom d'utilisateur MySQL]',
    'PASSWORD': '[Votre mot de passe MySQL]',
    'HOST': 'localhost',
    'PORT': '3306',
  }
}
```

# 5. Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

# 6. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

# 7. Lancer le serveur

```bash
python manage.py runserver
```

# 👤 Utilisation
 **🔐 Inscription et Connexion**
# Créez un compte depuis la page d’accueil, puis connectez-vous avec votre email ou téléphone et mot de passe.

# 🙍‍♂️ Profil Utilisateur
 **Accédez à votre profil pour :**
 - Modifier vos informations
 - Définir votre point de départ
 - Indiquer vos horaires habituels
 - Ajouter les détails du véhicule (si conducteur)

# 🧭 Matching des trajets
 Les passagers reçoivent automatiquement une liste de conducteurs proches selon l’horaire et le lieu.
 Les conducteurs reçoivent des demandes ciblées de passagers en attente.

# 🗺️ Carte Interactive
 Notre application offre la possibilité d’afficher une carte géographique interactive et précise pour visualiser les trajets ou zones couvertes.

# 🔑 Récupération de mot de passe
 En cas d’oubli du mot de passe, utilisez le lien “Mot de passe oublié ?” sur la page de connexion pour recevoir un email de réinitialisation.

 ---
 **Ainsi , l'interface de notre application vous garantit une expérience utilisateur unique !**
 ---

**© IFRI / UAC – Licence 1 Informatique – 2025**
