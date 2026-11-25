# Sprint 5 Planning — ERP Django
## Semanas W16–W18 · Espiral 6: Celery e Integraciones

**Sprint Goal:**
Al finalizar el Sprint 5, el ERP ejecutará tareas pesadas de forma
asíncrona con Celery+Redis: correos de confirmación, alertas de
stock bajo y reporte diario de ventas.

## Sprint Backlog — actualización W17

| Tarea | Estado |
|---|---|
| pip install celery redis flower | ✅ W16 |
| core/celery.py + tareas placeholder | ✅ W16 |
| pip install django-anymail[sendgrid]==10.3 | ✅ W17 |
| EMAIL_BACKEND configurado (console dev / SendGrid prod si hay API Key) | ✅ W17 |
| correo_enviado en Pedido + migración 0004 | ✅ W17 |
| Template confirmacion_pedido.html + .txt | ✅ W17 |
| Template alerta_stock.html + .txt | ✅ W17 |
| enviar_confirmacion_pedido: correo real + idempotencia + retry | ✅ W17 |
| verificar_stock_bajo: alerta al admin | ✅ W17 |
| 12 tests con mail.outbox (9 guía + 3 regresión) | ✅ W17 |
| render.yaml: SENDGRID_API_KEY, DEFAULT_FROM_EMAIL, ADMIN_EMAIL | ✅ W17 |
| Sender verificado en SendGrid + prueba real en Render | ⏳ W17 (en Render) |
| Celery Beat + tareas programadas | ⏳ W18 |

## DoD — Sprint 5
- Logs de Render: worker de Celery embebido "ready" y procesa tareas
- Webhook payment_intent.succeeded → tarea de correo en la cola (no espera)
- Correo de confirmación recibido en < 30 s (W17)
- Alerta de stock enviada cuando stock < umbral (W17)
- Reporte diario ejecutado a las 8:00 AM (W18)
- python manage.py test → ≥ 155 tests OK
