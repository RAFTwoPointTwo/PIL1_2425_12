from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' , views.register , name = 'register'),
    path('password_reset_form/' , auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html') , name = 'password_reset_form'),
    path('password_reset_done/' , auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html') , name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html') , name = 'password_reset_confirm'),
    path('reset/done/' , auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html') , name = 'password_reset_complete'),
    path('principale/' , views.principale , name = 'principale'),
    path('login/', views.login_view, name='login'),
    path('compte_cree/' , views.created_account , name = 'compte_cree'),
    path('map_page/', views.map_page, name='map_page'),
    
    path('messages/inbox/', views.inbox, name='inbox'),
    path('messages/envoyer/', views.send_message, name='send_message'),
    path('matching_page/', views.matching_page, name='matching_page'),
    path('profil/' , views.profil , name='profile'),
    path('profile_updating/' , views.profile_update , name='profile_update')
]