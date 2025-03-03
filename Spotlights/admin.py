from django.contrib import admin

from Spotlights.models import Spotlight


# Register your models here.
class SpotlightAdmin(admin.ModelAdmin):
    fields = ('ref', 'etat', 'disponible')
    readonly_fields = ('ref', 'etat', 'disponible')

admin.site.register(Spotlight, SpotlightAdmin)