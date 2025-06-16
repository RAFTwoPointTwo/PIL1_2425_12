from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
from .views import CustomLoginView,inbox, CustomLogoutView, send_message, chat_room, matching_page, enregistrer_trajet
=======
from .views import login_view
>>>>>>> 6b197e8642647d1b309759de1ce05eb2664d825e

urlpatterns = [
    path('' , views.register , name = 'register'),
   # path('login/' , auth_views.LoginView.as_view(template_name = 'login.html') , name = 'login'),
   # path('logout/' , auth_views.LogoutView.as_view(next_page = 'login') , name = 'logout'),
    path('password_reset/' , auth_views.PasswordResetView.as_view(template_name = 'password_reset.html') , name = 'password_reset'),
    path('password_reset_done/' , auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html') , name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = 'password_template_confirm.html') , name = 'password_reset_confirm'),
    path('reset/done/' , auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html') , name = 'password_reset_complete'),
   # path('profil/' , views.profil , name = 'profil'),
    path('principale/' , views.principale , name = 'principale'),
    #path('login/',CustomLoginView, name='login'),
    path('login/', login_view, name='login'),
    path('/compte_cree' , views.created_account , name = 'compte_cree'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('matching_page/', views.matching_page, name='matching_page'),
    path('enregistrer/', views.enregistrer_trajet, name='enregistrer'),
    path('messages/inbox/', views.inbox, name='inbox'),
    path('messages/envoyer/', views.send_message, name='send_message'),
    path('listes_des_utilisateurs/', views.listes_des_utilisateurs, name='listes_des_utilisateurs'),
]