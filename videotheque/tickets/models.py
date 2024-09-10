from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ticket(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.titre} - {self.date_creation}'
    
    
    
