# from django import forms
from django.forms import ModelForm
from .models import Film

class FilmForm(ModelForm):
    
    class Meta:
        model = Film
        # fields = '__all__'
        fields = ['titre', 'realisateur']