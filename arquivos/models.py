from django.db import models


class Documentos(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to="documentos/")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo