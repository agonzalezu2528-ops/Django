# Sprint 5 Retrospective — ERP Django
## Semanas W16–W18 · Espiral 6: Celery e Integraciones

**Fecha:** 25/11/2026

## ¿Qué funcionó bien? (Keep)
1. El campo `correo_enviado` en `Pedido` evitó correos duplicados (reintentos
   de Stripe y de Celery) sin un sistema externo de idempotencia.
2. `@override_settings(EMAIL_BACKEND=locmem)` hizo triviales los tests de
   correo: `mail.outbox` captura todo sin enviar nada.
3. Modo EAGER sin `REDIS_URL`: se desarrollaron y probaron todas las tareas
   sin Redis ni worker.
4. El webhook como único disparador del correo, con `try/except`: si Redis
   falla, el pago queda registrado y Stripe recibe 200.
5. Worker y Beat embebidos en el contenedor web: Celery funciona en el plan
   gratuito de Render (sin Background Workers).
6. La hora del reporte se configura con `REPORTE_DIARIO_HORA` sin tocar código.

## ¿Qué mejorar? (Improve)
1. **Dependencias:** `kombu` 5.7.0 exige `redis>=6.1` y el proyecto usa
   `redis==5.0.1`. En EAGER no se nota. Se fijó `kombu==5.3.7` y se agregó
   `tests/test_w18_dependencias.py`.
2. **Trabajar en la copia equivocada:** hay varias copias del proyecto en
   distintas carpetas y unidades; una edición cayó en `C:\Temp_Workspace_ERP`
   en vez de `D:\WorkSpace_ERP`. Abrir siempre el editor con la ruta correcta
   y usar git como fuente de verdad entre las dos máquinas.
3. **Archivos pegados incompletos:** `docker-entrypoint.sh` perdió el bloque de
   arranque de Gunicorn y `render.yaml` tuvo un bloque duplicado. Revisar con
   `Select-String` y con `git diff` antes de cada commit.
4. **Render Free se duerme:** Beat no dispara mientras el servicio duerme; se
   necesita un ping externo cada 10 minutos.
5. **Verificación en Render pendiente:** el reporte programado y el correo
   recibido en producción se confirman al desplegar.

## Acción de mejora (Kaizen) para Sprint 6
> "En el Sprint 6 no regeneraré `requirements.txt` con `pip freeze`: agregaré
>  solo la dependencia nueva y correré `pip check` antes de cada push. Antes
>  de cada commit revisaré `git status` y `git diff` para confirmar que edité
>  la carpeta correcta."

## Velocidad del Sprint 5

| HU | Pts plan. | Pts ent. |
|---|---|---|
| HU-E6-01 Infraestructura Celery+Redis | 3 | 3 |
| HU-E6-02 Tareas sin bloquear HTTP | 2 | 2 |
| HU-E6-03 Correo confirmación post-pago | 5 | 5 |
| HU-E6-04 Alerta stock bajo | 3 | 3 |
| HU-E6-05 Reporte diario 8 AM | 3 | 3 |
| HU-E6-06 Monitorear con Flower | 2 | 2 |
| **Total** | **18** | **18** |

**Velocidad Sprint 5:** 18 puntos
**Velocidad acumulada (S0–S5):** 123 puntos (según la guía; confirmar con el asesor)
**Tests al cierre:** 191 (OK, 8 omitidos por WeasyPrint/GTK en Windows)