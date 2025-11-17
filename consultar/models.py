from django.db import models

class Detalhes(models.Model):
    cnpj = models.CharField(max_length=18, null=False)
    consultor = models.CharField(max_length=120, null=False)
    filial = models.CharField(max_length=50, null=False)
    unidade = models.CharField(max_length=50, null=False)
    cliente = models.CharField(max_length=120)
    M = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'detalhes'