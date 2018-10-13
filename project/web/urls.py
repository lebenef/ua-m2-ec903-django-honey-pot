from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('condutil/', views.condutil, name="condutil"),
    path('donneeperso/', views.donneeperso, name='doneeperso'),
    path('menleg/', views.menleg, name='menleg'),

]
