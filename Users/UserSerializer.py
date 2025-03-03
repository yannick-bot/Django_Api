from rest_framework import serializers

from Users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # On spécifie le modèle associé
        fields = ('id', 'prenom', 'nom','email', 'password')