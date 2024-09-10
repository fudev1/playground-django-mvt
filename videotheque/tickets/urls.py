from django.urls import path
from . import views

urlpatterns = [ 
    path('creer/', views.creer_ticket, name="creer_ticket"),
    path('liste/', views.liste_tickets, name="liste_tickets"),
    path('modifier/<int:pk>/', views.modifier_ticket, name="modifier_ticket"),
    path('supprimer/<int:pk>/', views.supprimer_ticket, name="supprimer_ticket"),
]