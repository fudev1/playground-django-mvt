from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Realisateur) 
admin.site.register(models.Film)
admin.site.register(models.Acteur)
