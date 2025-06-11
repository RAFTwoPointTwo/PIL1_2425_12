from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request , 'home.html')

def principale(request):
    return render(request , 'principale.html')

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST , request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('principale')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request , 'register.html' , {'user_form' : user_form , 'profile_form' : profile_form})


@login_required
def profil(request):
    profile = request.user.profile
    return render(request , 'profil.html' , {'profile' : profile})

@login_required
def profil_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST , request.FILES , instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = ProfileUpdateForm(instance=profile)
        return render(request , 'profil_edit.html' , {'form' : form})

'''def map_shower():
'''

