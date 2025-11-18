from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
import datetime

class Usuarios(AbstractUser):
    unidade = models.CharField(max_length=50, blank=True)
    filial = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.username} + {self.unidade}"

class LoginToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        now = timezone.now()
        return now < self.created_at + datetime.timedelta(minutes=10)
    
    def __str__(self):
        return f"Token para {self.user}"