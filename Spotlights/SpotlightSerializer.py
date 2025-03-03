from rest_framework import serializers

from Spotlights.models import Spotlight


class SpotlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spotlight
        fields = ('id', 'ref', 'etat', 'disponible')