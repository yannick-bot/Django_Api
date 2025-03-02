from django.db import models

# Create your models here.
class Spotlight(models.Model):
    ref = models.CharField(max_length=100)
    etat = models.CharField(max_length=100)
    disponible = models.BooleanField()