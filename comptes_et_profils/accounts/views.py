from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomLoginForm , ProfileForm


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
            return redirect('principale')
        else:
            print(f"user_form errors : {user_form.errors}")
            print(f"prof errors : {profile_form.errors}")
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

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

class CustomLoginView(LoginView):
    template_name='login.html'
    authentification_form=CustomLoginForm

class CustomLogoutView(LogoutView):
    next_page='/login/'    


