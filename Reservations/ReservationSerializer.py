from rest_framework import serializers

from Reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'user_id', 'spot_id', 'h_debut', 'h_fin')