import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import LoginToken

@login_required
def solicitar_token(request):
    if request.method == 'POST':
        token_code = str(random.randint(100000, 999999))

        LoginToken.objects.filter(user=request.user).delete()
        LoginToken.objects.create(user=request.user, token=token_code)
    
        send_mail(
            'Seu Token de Acesso',
            f'Olá, seu código de verificação é: {token_code}',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False,
        )

        messages.success(request, 'Token enviado com sucesso para o e-mail!')
        return redirect('validar_token')
    
    return render(request, 'token/solicitar_token.html')

@login_required
def validar_token(request):
    if request.method == 'POST':
        token_input = request.POST.get('token')

        token_obj = LoginToken.objects.filter(user=request.user).last()

        if token_obj and token_obj.token == token_input:
            if token_obj.is_valid(): 

                request.session['token_validado'] = True

                request.session.modified = True
                
                token_obj.delete()
                return redirect('consulta-cnpj')
            else:
                messages.error(request, 'Este token expirou. Solicite um novo.')
        else:
            messages.error(request, 'Token inválido.')

    return render(request, 'token/validar_token.html')