from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InscriptionForm(UserCreationForm):
    class Meta: # permet d'aller rechercher tous les champs de l'utilisateur
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # fields = '__all__'
