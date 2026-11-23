# Sprint 4 Planning — ERP Django
## Semanas W13–W15 · Espiral 5: E-commerce y Pagos

**Sprint Goal:**
Al finalizar el Sprint 4, el ERP tendrá catálogo filtrable,
carrito de compras y pago completo con Stripe sandbox,
actualizando automáticamente el estado del pedido.

## Sprint Backlog — actualización W13

| Tarea | Estado |
## Sprint 4 — Estado final W15

| HU | Estado | Pts |
|---|---|---|
| HU-E5-01 a HU-E5-08 | ✅ Completadas | 26/26 |

## Hito M5 — ALCANZADO ✅
- Catálogo: /catalogo/ → 200 sin auth con filtros
- Carrito: agregar/remover/actualizar/vaciar funcional
- Stripe: tarjeta 4242 → pago exitoso → pedido 'pagado'
- Webhook: payment_intent.succeeded → stock decrementado
- Tests: Ran 147 tests → OK
- Fecha: ___/___/_____

## DoD — Sprint 4
- GET /catalogo/ → 200 sin autenticación con lista de productos
- Filtrar por categoría → solo productos de esa categoría
- Agregar producto al carrito → contador en navbar se incrementa
- Tarjeta de prueba Stripe 4242... → pedido cambia a "pagado"
- Webhook verifica firma → stock se descuenta
- python manage.py test → ≥ 131 tests OK
