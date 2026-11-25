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


## Sprint 5 — Estado final W18

| HU | Historia | Estado | Pts |
|---|---|---|---|
| HU-E6-01 | Infraestructura Celery+Redis funcional | ✅ Completada | 3 |
| HU-E6-02 | Tareas sin bloquear HTTP | ✅ Completada | 2 |
| HU-E6-03 | Correo de confirmación post-pago | ✅ Completada | 5 |
| HU-E6-04 | Correo de alerta de stock bajo | ✅ Completada | 3 |
| HU-E6-05 | Reporte diario de ventas a las 8 AM | ✅ Completada | 3 |
| HU-E6-06 | Monitorear tareas con Flower | ✅ Completada | 2 |
| **Total** | | | **18/18** |

## Sprint Backlog — actualización W18

| Tarea | Estado |
|---|---|
| reporte_ventas_diario: annotate + Sum(F('cantidad') * F('precio_unitario')) | ✅ W18 |
| Top 5 incluye compras en línea (Pedido.items_snapshot) | ✅ W18 |
| Templates reporte_ventas.html + .txt | ✅ W18 |
| CELERY_BEAT_SCHEDULE: crontab (reporte) + timedelta (stock) | ✅ W18 |
| Hora configurable REPORTE_DIARIO_HORA | ✅ W18 |
| Beat embebido en el worker (--beat, CELERY_EMBEDDED_BEAT) | ✅ W18 |
| kombu==5.3.7 compatible con redis==5.0.1 | ✅ W18 |
| Acción admin "Enviar correo de confirmación" | ✅ W18 |
| Suite completa en verde: 191 tests, skipped=8 | ✅ W18 |
| Verificación en Render (Logs y correo del reporte) | Pendiente |

## Hito M6
- Tests: Ran 191 tests → OK (8 omitidos: PDF requiere GTK, corre en Render/Linux)
- Beat y worker embebidos en el contenedor web de Render, una sola instancia
- Pendiente de declarar: confirmar en Render `beat: Starting...` y el correo del reporte