from django.urls import path
from .views import DetalheView

urlpatterns = [
    path("consulta-cnpj/", DetalheView, name="consulta-cnpj"),
]
