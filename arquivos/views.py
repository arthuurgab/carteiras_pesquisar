from django.shortcuts import render
from .models import Documentos

def lista_documentos(request):
    docs = Documentos.objects.all().order_by("-criado_em")
    return render(request, "arquivos.html", {"documentos": docs}) 