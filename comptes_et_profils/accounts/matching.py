from .models import CustomUser,Matching, Trajet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime


def matching(request):
    utilisateur=request.user.customuser
    utilisant=
    groupe1=[]
    for utilisant in CustomUser.objects.all():
      if  utilisant.role == 'conducteur' and utilisant != utilisateur:
        trajet = Matching.objects.filter(conducteur=utilisant)
        if trajet.exists():
            for t in trajet:
                if t.start_point == utilisateur.start_point and t.start_date >= datetime.datetime.now().time():
                    groupe1.append(t)
