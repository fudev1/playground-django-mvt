from django.urls import path
from . import views


urlpatterns = [
    path('', views.liste_film, name='liste'),
    path('supprimer/', views.supprimer_film, name='supprimer_film'),
    path('creer/', views.creation_film, name='creer_film'),
    path('realisateur/creer/', views.ajouter_realisateur, name='ajouter_realisateur'),
    path('acteur/creer/', views.ajouter_acteur, name='ajouter_acteur'),
    
]
