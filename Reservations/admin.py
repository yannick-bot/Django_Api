from django.contrib import admin

from Reservations.models import Reservation


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    fields = ('user_id', 'spot_id', 'h_debut', 'h_fin')
    readonly_fields = ('user_id', 'spot_id', 'h_debut', 'h_fin')

admin.site.register(Reservation, ReservationAdmin)