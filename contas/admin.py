from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios

class UsuariosAdmin(UserAdmin):
    model = Usuarios
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('unidade', 'filial')}),
    )

admin.site.register(Usuarios, UsuariosAdmin)
