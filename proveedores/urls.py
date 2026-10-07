# proveedores/urls.py
"""URLs de la app proveedores — W02."""
from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.index, name='inicio'),
]