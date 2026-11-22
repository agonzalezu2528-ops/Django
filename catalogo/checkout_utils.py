# catalogo/checkout_utils.py
"""Funciones auxiliares para el proceso de checkout — W14.

Separadas de views.py para facilitar las pruebas unitarias.
"""
from decimal import Decimal, ROUND_HALF_UP
from datetime import date

from django.conf import settings

from clientes.models      import Cliente
from configuracion.models import ConfiguracionERP
from ventas.models        import Pedido


def calcular_totales(carrito: dict) -> dict:
    """Calcula subtotal, IVA y total del carrito.

    Args:
        carrito: dict de sesión con estructura
                 {str(pk): {precio: str, cantidad: int, ...}}

    Returns:
        dict con subtotal, iva_pct, iva_monto, total (todos Decimal).
    """
    config   = ConfiguracionERP.get_instance()
    iva_pct  = config.iva_porcentaje / Decimal('100')

    # [ADAPTADO] valor inicial Decimal('0.00') para que sum() siempre
    # devuelva Decimal (sin valor inicial, un carrito vacío daría int 0).
    subtotal = sum(
        (Decimal(datos['precio']) * int(datos['cantidad'])
         for datos in carrito.values()),
        Decimal('0.00')
    )
    iva_monto = (subtotal * iva_pct).quantize(
        Decimal('0.01'), rounding=ROUND_HALF_UP
    )
    total = subtotal + iva_monto

    return {
        'subtotal':  subtotal,
        'iva_pct':   config.iva_porcentaje,
        'iva_monto': iva_monto,
        'total':     total,
    }


def armar_items(carrito: dict) -> list:
    """Convierte el carrito de sesión en una lista con el subtotal por línea.

    Los templates de Django no pueden multiplicar (precio × cantidad),
    por eso el cálculo se hace aquí.

    Returns:
        list de dicts con nombre, precio, cantidad y subtotal (Decimal).
    """
    items = []
    for datos in carrito.values():
        precio   = Decimal(datos['precio'])
        cantidad = int(datos['cantidad'])
        items.append({
            'nombre':   datos['nombre'],
            'precio':   precio,
            'cantidad': cantidad,
            'subtotal': precio * cantidad,
        })
    return items


def obtener_o_crear_cliente(user) -> Cliente:
    """Obtiene o crea un Cliente del ERP vinculado al usuario Django.

    Usa el correo del usuario si existe; si no, genera uno temporal.

    Args:
        user: instancia de django.contrib.auth.models.User.

    Returns:
        Cliente: instancia del modelo Cliente del ERP.
    """
    correo = user.email or f"{user.username}@erp.local"
    nombre = (
        user.get_full_name() or user.username
    )

    cliente, _ = Cliente.objects.get_or_create(
        correo=correo,
        defaults={'nombre': nombre, 'activo': True}
    )
    # Actualizar nombre si el usuario tiene nombre completo
    if cliente.nombre != nombre and user.get_full_name():
        cliente.nombre = nombre
        cliente.save(update_fields=['nombre'])

    return cliente


def generar_numero_pedido() -> str:
    """Genera un número de pedido único con formato PED-YYYY-NNNN.

    [ADAPTADO] La guía usa count() + 1, que puede repetir un número si
    se borra un pedido intermedio (numero_pedido es unique=True y daría
    IntegrityError). Aquí se toma el número más alto del año y se suma 1.

    Returns:
        str: por ejemplo 'PED-2026-0001'
    """
    anio    = date.today().year
    prefijo = f'PED-{anio}-'
    ultimo  = (
        Pedido.objects
        .filter(numero_pedido__startswith=prefijo)
        .order_by('-numero_pedido')
        .values_list('numero_pedido', flat=True)
        .first()
    )
    siguiente = int(ultimo.rsplit('-', 1)[1]) + 1 if ultimo else 1
    return f'{prefijo}{siguiente:04d}'
