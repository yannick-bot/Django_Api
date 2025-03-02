from django.db import models
from django.db.models import ManyToManyField

from Spotlights.models import Spotlight
from Users.models import User


# Create your models here.
class Reservation(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    spot_id = models.OneToOneField(Spotlight, on_delete=models.CASCADE)
    h_debut = models.DateField()
    h_fin = models.DateField()

