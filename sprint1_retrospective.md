# Sprint 1 Retrospective — ERP Django
## Semanas W04–W06 · Espiral 2: Modelado de Datos y ORM

**Fecha:** ___/___/_____

## ¿Qué funcionó bien? (Keep)
1. Diseñar el ER en papel antes de escribir código evitó errores de FK.
2. Los smoke tests de W05 detectaron un bug en precio_unitario is None.
3. Jazzmin mejora significativamente la UX del admin.

## ¿Qué mejorar? (Improve)
1. Documentar el diagrama ER con más detalle antes de la revisión.
2. Ejecutar full_clean() en los tests desde el principio (no solo save()).

## Acción de mejora (Kaizen) para Sprint 2
> "En el Sprint 2, voy a crear primero los archivos de template
>  y las urls.py antes de escribir las vistas, para no repetir
>  el error de W01 donde las vistas estaban en urls.py."

## Velocidad del Sprint 1

| HU | Puntos planificados | Puntos entregados |
|---|---|---|
| HU-E2-01 Diagrama ER aprobado | 3 | 3 |
| HU-E2-02 Modelo Cliente | 2 | 2 |
| HU-E2-03 Modelo Proveedor | 2 | 2 |
| HU-E2-04 Modelo Categoria | 1 | 1 |
| HU-E2-05 Modelo Producto | 3 | 3 |
| HU-E2-06 Modelos Venta + Detalle | 5 | 5 |
| HU-E2-07 Suite ≥ 15 tests | 3 | 3 |
| HU-E2-08 Admin con Jazzmin | 2 | 2 |
| **Total** | **21** | **21** |

**Velocidad del equipo Sprint 1:** 21 puntos
**Velocidad acumulada (S0 + S1):** 31 puntos