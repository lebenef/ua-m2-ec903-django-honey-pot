from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('condutil/', views.condutil, name="Condition d'utilisation"),
    path('donneeperso/', views.donneeperso, name='Données Personelles'),
    path('menleg/', views.menleg, name='Mention Legal'),

]
