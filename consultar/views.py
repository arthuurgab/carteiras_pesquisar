from django.shortcuts import render, redirect
from .models import Detalhes
from datetime import datetime
from django.contrib.auth.decorators import login_required
from contas.decorators import token_required

@token_required
def DetalheView(request):
    data = datetime.now().year

    dados = None
    erro = None

    if request.method == 'POST':
        cnpj = request.POST.get("cnpj", "")
        cnpj = "".join(filter(str.isdigit, cnpj))
        
        try: 
            detalhes = Detalhes.objects.get(cnpj=cnpj)
            dados = {
                "cliente": detalhes.cliente,
                "consultor": detalhes.consultor,
                "unidade": detalhes.unidade,
                "filial": detalhes.filial,
                "meses": detalhes.M
            }

            request.session["dados_cnpj"] = dados
            return redirect("consulta-cnpj")
        except Detalhes.DoesNotExist:
            request.session["erro_cnpj"] = "CNPJ não encontrado."
            return redirect("consulta-cnpj")
    
    dados = request.session.pop("dados_cnpj", None)
    erro = request.session.pop("erro_cnpj", None)
    return render(request, "detalhes.html", {"dados": dados, "erro": erro, "data": data})