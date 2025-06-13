from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView,CustomLogoutView

urlpatterns = [
    path('home/' , views.home , name = 'home'),
    path('register/' , views.register , name = 'register'),
   # path('login/' , auth_views.LoginView.as_view(template_name = 'login.html') , name = 'login'),
   # path('logout/' , auth_views.LogoutView.as_view(next_page = 'login') , name = 'logout'),
    path('password_reset/' , auth_views.PasswordResetView.as_view(template_name = 'password_reset.html') , name = 'password_reset'),
    path('password_reset_done/' , auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html') , name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = 'password_template_confirm.html') , name = 'password_reset_confirm'),
    path('reset/done/' , auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html') , name = 'password_reset_complete'),
    path('profil/' , views.profil , name = 'profil'),
    path('' , views.principale , name = 'principale'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',CustomLogoutView.as_view(), name='logout')
]