# contas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('solicitar_token/', views.solicitar_token, name="solicitar_token"),
    path('validar_token/', views.validar_token, name="validar_token")
]
