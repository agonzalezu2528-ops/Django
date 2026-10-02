# proveedores/urls.py
"""URLs de la app proveedores — W01 (mínimo funcional)."""
from django.urls import path
from django.http import HttpResponse

app_name = 'proveedores'


def bienvenida_proveedores(request):
    """Vista temporal de bienvenida para la app proveedores."""
    return HttpResponse(
        "<h2>📦 Módulo proveedores</h2>"
        "<p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )


urlpatterns = [
    path('', bienvenida_proveedores, name='inicio'),
]