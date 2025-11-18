from django.shortcuts import redirect
from functools import wraps

def token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')
        
        if not request.session.get('token_validado'):
            return redirect('solicitar_token')
        
        return view_func(request, *args, *kwargs)
    return _wrapped_view