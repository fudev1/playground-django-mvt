from django.shortcuts import render
from django.http import HttpResponse
from .data import films

# Create your views here.

def index(request):
    return HttpResponse("Helloooow")

def liste_film(request):
    # Avec l'import de data.py on peut récupérer le tableau et mapper les données
    return render(request, 'liste.html', {'films': films})


# def detail_film(request, id):
#     films = [
#         {"id": 1, "titre": "Pulp Fiction", "auteur": "Quentin Tarantino", "contenu": "Un film de fiction sur le début de la vie de John Travolta"},
#         {"id": 2, "titre": "La ligne verte", "auteur": "Frank Darabont", "contenu": "Un film de fiction sur le début de la vie de John Travolta"},
#         {"id": 3, "titre": "Gladiator", "auteur": "Ridley Scott", "contenu": "Un film de fiction sur le début de la vie de John Travolta"},
#     ]

#     film = next(film for film in films if film['id'] == id)