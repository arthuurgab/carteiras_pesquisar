from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuarios

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuarios
        fields = ('email', 'username')