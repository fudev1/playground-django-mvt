from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Profil
from .forms import *

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # d'habitude on aurait mit form.save() avec un redirect mais ici on va faire autre chose avec l'utilisateur
            # user = form.save()
            # login(request, user)
            # return redirect('index')

            utilisateur = form.save() # on récupère l'utilisateur créé par le formulaire
            profil = Profil.objects.create(utilisateur=utilisateur) # on crée un profil associé à l'utilisateur
            profil.generer_numero_employe() # on génère un numéro d'employe
            profil.save() # on sauvegarde le profil

            login(request, utilisateur) # on se connecte
            return redirect('index') # on redirige vers la page d'accueil
        
    else: 
        form = InscriptionForm()

    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            utilisateur = authenticate(request, username=username, password=password)
            if utilisateur is not None:
                login(request, utilisateur)
                return redirect('index')
            
    else: 
        form = AuthenticationForm()

    return render(request, 'connexion.html', {'form': form})


def deconnexion(request):
    logout(request)
    return redirect('index')
