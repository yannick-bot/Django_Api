from django.contrib import admin

from Users.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ('prenom', 'nom', 'email', 'password')
    readonly_fields = ('prenom', 'nom', 'email', 'password')

admin.site.register(User, UserAdmin)