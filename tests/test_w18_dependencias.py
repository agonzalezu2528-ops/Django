"""Regresión 2026-11-20 — compatibilidad kombu y redis-py, y acción del admin.

Abre el transporte Redis contra un puerto cerrado: debe fallar por
CONEXIÓN (no hay Redis local), nunca por versión.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import SimpleTestCase, TestCase, override_settings
from kombu import Connection
from kombu.exceptions import VersionMismatch

from clientes.models      import Cliente
from configuracion.models import ConfiguracionERP
from ventas.models        import Pedido


class KombuRedisCompatibilidadTest(SimpleTestCase):

    def test_transporte_redis_acepta_version_de_redis_py(self):
        conexion = Connection('redis://127.0.0.1:6399/0', connect_timeout=1)
        try:
            conexion.ensure_connection(max_retries=1, interval_start=0, interval_step=0)
            conexion.default_channel
        except VersionMismatch as exc:
            self.fail(f'kombu y redis-py incompatibles: {exc}')
        except Exception:
            pass   # esperado: no hay Redis en el laboratorio
        finally:
            conexion.release()


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    CELERY_TASK_ALWAYS_EAGER=True,
)
class AccionReenviarConfirmacionTest(TestCase):
    """Acción del admin: enviar correo a pagados con correo_enviado=False."""

    def setUp(self):
        ConfiguracionERP.get_instance()
        self.admin = get_user_model().objects.create_superuser(
            'root', 'root@test.com', 'x')
        self.client.force_login(self.admin)
        cli = Cliente.objects.create(nombre='C', correo='c@test.com')
        self.pagado = Pedido.objects.create(
            numero_pedido='PED-A-1', cliente=cli, estado='pagado',
            total_pagado=Decimal('30.16'))
        self.pendiente = Pedido.objects.create(
            numero_pedido='PED-A-2', cliente=cli, estado='pendiente')

    def test_envia_solo_pagados_sin_correo(self):
        resp = self.client.post('/admin/ventas/pedido/', {
            'action': 'reenviar_confirmacion',
            '_selected_action': [self.pagado.pk, self.pendiente.pk],
        })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('PED-A-1', mail.outbox[0].subject)
        self.pagado.refresh_from_db()
        self.assertTrue(self.pagado.correo_enviado)