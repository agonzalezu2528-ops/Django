# Ficha de Sistematización — Espiral 6
## ERP Django · Espiral E6: Celery e Integraciones
## UTEC Celaya · Técnico en Programación (SEP 3061300006-23)

| Campo | Contenido |
|---|---|
| **Número de espiral** | 6 |
| **Nombre del ciclo** | Celery e Integraciones |
| **Semanas** | W16 – W18 |
| **Fecha de inicio** | ___/___/_____ |
| **Fecha de cierre** | 25/11/2026 |
| **Responsable** | [Alan Gonzalez Urbina] |
| **Asesor** | MC. Román Fernando López González |

---

## 1. Objetivo del ciclo

Implementar procesamiento asíncrono con Celery y Redis para correos
transaccionales de confirmación de pedido, alertas de stock bajo y reportes
diarios automáticos con Celery Beat, con el laboratorio en modo EAGER (sin
Docker Desktop) y producción en el plan gratuito de Render.

---

## 2. Tareas realizadas

| # | Tarea | Estado | Semana |
|---|---|---|---|
| 1 | Celery + redis + flower; `core/celery.py` | ✅ | W16 |
| 2 | `CELERY_*` en settings: Redis si hay `REDIS_URL`, EAGER si no | ✅ | W16 |
| 3 | Worker embebido en `docker-entrypoint.sh` (`CELERY_EMBEDDED_WORKER=1`) | ✅ | W16 |
| 4 | Webhook `payment_intent.succeeded` como único disparador del correo | ✅ | W16 |
| 5 | `django-anymail[sendgrid]`; `Pedido.correo_enviado` (idempotencia) | ✅ | W17 |
| 6 | Templates `confirmacion_pedido` y `alerta_stock`; tareas de correo y stock | ✅ | W17 |
| 7 | Templates `reporte_ventas` (.html + .txt) | ✅ | W18 |
| 8 | `reporte_ventas_diario` con `annotate` + `Sum(F() * F())` y `items_snapshot` | ✅ | W18 |
| 9 | `CELERY_BEAT_SCHEDULE`: crontab (reporte) + timedelta (stock) | ✅ | W18 |
| 10 | `REPORTE_DIARIO_HORA` configurable (default 08:00) | ✅ | W18 |
| 11 | Beat embebido en el worker (`--beat`, `CELERY_EMBEDDED_BEAT`) | ✅ | W18 |
| 12 | `kombu==5.3.7` compatible con `redis==5.0.1` | ✅ | W18 |
| 13 | Acción admin: reenviar confirmación de pedidos pagados sin correo | ✅ | W18 |

---

## 3. Evidencias

- Pruebas: `python manage.py test tests` → **Ran 191 tests — OK (skipped=8)**
  (los 8 omitidos generan PDF con WeasyPrint y requieren GTK: corren en Render/Linux)
- Pruebas nuevas de W18: `test_w18_beat` (10) y `test_w18_dependencias` (2)
- Reporte diario en local: correo impreso en la terminal (modo EAGER)
- Logs de Render a verificar tras desplegar:
  - [ ] `Celery Beat embebido ACTIVADO (reporte diario HH:MM hora MX)`
  - [ ] `beat: Starting...` y `celery@... ready` sin `VersionMismatch`
  - [ ] `Scheduler: Sending due task reporte-ventas-diario-8am`
- [ ] Captura del correo de confirmación: `evidencias/espiral_06/correo_confirmacion.png`
- [ ] Captura del reporte diario: `evidencias/espiral_06/reporte_diario.png`

---

## 4. Criterios de aceptación

| Criterio | Estado |
|---|---|
| `correo_enviado=True` previene duplicados | ✅ |
| `reporte_ventas_diario` en `CELERY_BEAT_SCHEDULE` | ✅ |
| `verificar_stock_bajo` en `CELERY_BEAT_SCHEDULE` | ✅ |
| 191 tests OK | ✅ |
| Beat activo y reporte recibido en Render | Pendiente de verificar |

---

## 5. Problemas encontrados

| Problema | Causa | Solución aplicada |
|---|---|---|
| Sin Docker Desktop en el laboratorio | Política del equipo | Modo EAGER sin `REDIS_URL` |
| Render Free sin Background Workers | Plan gratuito | Worker y Beat embebidos en el contenedor web |
| `VersionMismatch` kombu / redis-py | `kombu` 5.7.0 con `redis` 5.0.1 | `kombu==5.3.7` + prueba de compatibilidad |
| Top de productos sin compras en línea | El checkout crea `Pedido`, no `Venta` | El top suma también `items_snapshot` |
| Edición en la carpeta equivocada | Varias copias del proyecto | Abrir el editor en `D:\WorkSpace_ERP` y comparar con `git diff` |
| `docker-entrypoint.sh` sin Gunicorn | Bloque perdido al pegar | Restaurado y verificado con `Select-String` |
| `requirements.txt` en UTF-16 | `pip freeze >` en PowerShell | Editar a mano / no usar redirección |

---

## 6. Lecciones aprendidas

1. El modo EAGER es ideal para desarrollar, pero oculta los errores de
   conexión con el broker: hay que probar el transporte real o al menos la
   compatibilidad de versiones.
2. La idempotencia (`correo_enviado`) se diseña desde el modelo.
3. ______________________________________________________________

---

## 7. Tiempo total invertido

| Categoría | Horas |
|---|---|
| Diseño | |
| Implementación | |
| Pruebas | |
| Documentación | |
| **Total Espiral 6** | |