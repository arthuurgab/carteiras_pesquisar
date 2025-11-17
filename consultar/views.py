from django.shortcuts import render
from .models import Detalhes

def DetalheView(request):
    dados = None
    erro = None

    if request.method == 'POST':
        cnpj = request.POST.get("cnpj")

        try: 
            dados = Detalhes.objects.get(cnpj=cnpj)
        except Detalhes.DoesNotExist:
            erro = "CNPJ não encontrado."
    
    return render(request, "detalhes.html", {"dados": dados, "erro": erro})