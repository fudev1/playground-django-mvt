# from django import forms
from django.forms import ModelForm
from .models import Film, Realisateur, Acteur
from django import forms


class Ajouter_Film(ModelForm):
    class Meta:
        model = Film
        # fields = '__all__'
        fields = ['titre', 'realisateur', 'acteurs']


class Supprimer_Film(forms.Form):
    titre = forms.CharField(max_length=100)
    date_sortie = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))


"""
Si tu veux que Django puisse automatiquement gérer la création et la sauvegarde d'un objet dans la base de données, 
il est préférable d'utiliser un formulaire basé sur un modèle avec `forms.ModelForm` au lieu de `forms.Form`
=> Permet à Django de lier le formulaire à un modèle et de faciliter l'appel de la méthode `.save()`

ModelForm : Django s'attend à ce que tu crées ou mette à jour un objet de modèle pour la base de données
forms.Form : Recueillir des infos pour supprimer (avec une autre méthode ensuite)
"""

# ERREUR DE FAIRE CECI : (voir doc)
# Pour modifier l'objet > db > utiliser ModelForm

# class Ajouter_Acteur(forms.Form):
#     nom = forms.CharField(max_length=100)
#     prenom = forms.CharField(max_length=100)


class Ajouter_Realisateur(ModelForm):
    class Meta: 
        model = Realisateur
        fields = '__all__'
    
    def clean_nom(self):
        nom = self.cleaned_data['nom']
        if 'batman' in nom.lower():
            raise forms.ValidationError('Zemmour est un acteur interdit')
        
        return nom
    

class Ajouter_Acteur(ModelForm):
    class Meta:
        model = Acteur
        fields = '__all__'


    # clean est une méthode spéciale de Django
    # _nom est une variable interne de la classe Form (il fait le lien entre le formulaire et le modèle)
    def clean_nom(self):
        nom = self.cleaned_data['nom']
        if 'batman' in nom.lower():
            raise forms.ValidationError('Zemmour est un acteur interdit')
        
        return nom
    


