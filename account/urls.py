from django.contrib.auth.views import login, logout
from django.urls import path

from . import views


app_name = 'account'
urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', login, {'template_name': 'account/login.html'}, name='login'),
    path('sair/', logout, {'next_page': 'core:index'}, name='logout'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password'),
    path('registro/', views.register, name='register'),
]
