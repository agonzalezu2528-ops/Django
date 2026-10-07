# ventas/urls.py
"""URLs de la app ventas — W02."""
from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.index, name='inicio'),
]