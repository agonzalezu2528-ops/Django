# reportes/urls.py
"""URLs de la app reportes — W02."""
from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.index, name='inicio'),
]