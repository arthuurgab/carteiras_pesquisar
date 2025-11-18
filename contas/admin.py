from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios

class UsuariosAdmin(UserAdmin):
    model = Usuarios
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('unidade', 'filial')}),
    )

admin.site.register(Usuarios, UsuariosAdmin)
