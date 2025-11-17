from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    unidade = models.CharField(max_length=50, blank=True)
    filial = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.username} + {self.unidade}"
