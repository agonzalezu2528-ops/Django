# core/views.py
"""Vistas principales del proyecto ERP â€” W02.
MigraciÃ³n: HttpResponse â†’ render() con templates y contexto.
"""
from django.shortcuts import render
from django.urls import reverse


def bienvenida(request):
    """PÃ¡gina de inicio del ERP con tarjetas de mÃ³dulos.

    Context:
        modulos (list): Lista de dicts con icono, nombre, url y descripcion.

    Returns:
        HttpResponse con template bienvenida.html.
    """
    modulos = [
        {
            'nombre': 'Productos',
            'icono': 'ðŸ“¦',
            'url': reverse('productos:lista'),
            'descripcion': 'Inventario, precios y stock',
        },
        {
            'nombre': 'Clientes',
            'icono': 'ðŸ‘¥',
            'url': reverse('clientes:lista'),
            'descripcion': 'Cartera y gestiÃ³n de clientes',
        },
        {
            'nombre': 'Proveedores',
            'icono': 'ðŸ­',
            'url': reverse('proveedores:lista'),
            'descripcion': 'Red de proveedores',
        },
        {
            'nombre': 'Ventas',
            'icono': 'ðŸ’°',
            'url': reverse('ventas:lista'),
            'descripcion': 'Pedidos, facturas y cobros',
        },
        {
            'nombre': 'Reportes',
            'icono': 'ðŸ“Š',
            'url': reverse('reportes:inicio'),
            'descripcion': 'Dashboard y analÃ­tica',
        },
        {
            'nombre': 'Admin',
            'icono': 'âš™ï¸',
            'url': '/admin/',
            'descripcion': 'Panel de administraciÃ³n Django',
        },
    ]
    return render(request, 'bienvenida.html', {'modulos': modulos})
