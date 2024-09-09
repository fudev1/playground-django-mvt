from django.shortcuts import redirect, render
from django.http import HttpResponse
from .data import films
from .forms import Supprimer_Film, Ajouter_Film, Ajouter_Acteur, Ajouter_Realisateur
from .models import Acteur, Film

# Create your views here.

def index(request):
    return HttpResponse("Helloooow")

def liste_film(request):
    # Avec l'import de data.py on peut récupérer le tableau et mapper les données
    return render(request, 'liste.html', {'films': films})

def liste_acteur(request):
    all_acteurs = Acteur.objects.all()


def supprimer_film(request):
    form = Supprimer_Film

    # Faire quelque chose quand c'est GET
    if request.method == 'GET':
        return render(request, 'supprimer_film.html', {'form': form})
    
    # Faire quelque chose quand c'est POST
    form_retour = form(request.POST)
    if form_retour.is_valid():
        titre = form_retour.cleaned_data['titre']
        date_sortie = form_retour.cleaned_data['date_sortie']
        return HttpResponse(f'Vous avez supprimé le film : {titre} - {date_sortie}')
    
    return HttpResponse('Formulaire envoyé mais pas valide')

def ajouter_film(request):
    if request.method == "POST":
        form = Ajouter_Film(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste')
        
    else: 
        form = Ajouter_Film()
        
    return render(request, 'ajouter_film.html', {'form': form})


def ajouter_realisateur(request):
    if request.method == "POST":
        form = Ajouter_Realisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste')
    else:
        form = Ajouter_Realisateur()
        
    return render(request, "ajouter_realisateur.html", {'form': form})

        
def ajouter_acteur(request):
    if request.method == "POST":
        form = Ajouter_Acteur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste')

    # permet de garder les données de l'utilisateur
    else:
        form = Ajouter_Acteur()
    
    return render(request, "ajouter_acteur.html", {'form': form})



def detail_film(request, pk):
    film = Film.objects.get(id=pk)
    
    return render(request, 'detail_film.html', {'film': film})