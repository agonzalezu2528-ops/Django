# clientes/urls.py
"""URLs de la app clientes — W02."""
from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.index, name='inicio'),
]