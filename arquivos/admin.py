from django.contrib import admin
from .models import Documentos

@admin.register(Documentos)
class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'criado_em')
    search_fields = ['titulo']