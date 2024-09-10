from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = [
    ('open', 'Ouvert'),
    ('in_progress', 'En cours'),
    ('closed', 'Fermé'),
]

class Ticket(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.RESTRICT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f'{self.titre} - {self.date_creation}'
    
    
    
