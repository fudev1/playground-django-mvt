from django.db import models

# Create your models here.



class Realisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.prenom} {self.nom}'
    
class Acteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.prenom} {self.nom}'


class Film(models.Model):
    titre = models.CharField(max_length=100)
    resume = models.TextField(null=True)
    date_sortie = models.DateField(null=True)
    realisateur = models.ForeignKey(Realisateur, on_delete=models.RESTRICT)
    acteurs = models.ManyToManyField(Acteur)
    genre = models.CharField(max_length=100, null=True)
    url_affiche = models.URLField(null=True)
    rating = models.FloatField(null=True)


    def __str__(self):
        return f'ID: {self.id} - {self.titre} ({self.date_sortie} - {self.realisateur})'
    





