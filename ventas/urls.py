# ventas/urls.py
"""URLs de la app ventas — W01 (mínimo funcional)."""
from django.urls import path
from django.http import HttpResponse

app_name = 'ventas'


def bienvenida_ventas(request):
    """Vista temporal de bienvenida para la app ventas."""
    return HttpResponse(
        "<h2>📦 Módulo ventas</h2>"
        "<p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )


urlpatterns = [
    path('', bienvenida_ventas, name='inicio'),
]