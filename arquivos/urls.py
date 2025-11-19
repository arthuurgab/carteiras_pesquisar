from django.urls import path
from . import views

urlpatterns = [
    path("documentos/", views.lista_documentos, name="lista_documentos"),
]