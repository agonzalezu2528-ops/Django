# Sprint 4 Planning — ERP Django
## Semanas W13–W15 · Espiral 5: E-commerce y Pagos

**Sprint Goal:**
Al finalizar el Sprint 4, el ERP tendrá catálogo filtrable,
carrito de compras y pago completo con Stripe sandbox,
actualizando automáticamente el estado del pedido.

## Sprint Backlog — actualización W13

| Tarea | Estado |
|---|---|
| App catalogo + django-filter | ✅ W13 |
| ProductoFilter (nombre/categoría/precio) | ✅ W13 |
| CatalogoView pública con paginación | ✅ W13 |
| Carrito en sesión (agregar/remover/actualizar/vaciar) | ✅ W13 |
| Context processor carrito_info | ✅ W13 |
| Template catalogo.html con tarjetas | ✅ W13 |
| Template carrito.html con tabla | ✅ W13 |
| Contador carrito en navbar base.html | ✅ W13 |
| 8 tests de e-commerce | ✅ W13 |
| Checkout con Stripe sandbox | ⏳ W14 |
| Webhooks y estados de pedido | ⏳ W15 |

**Total Sprint 4:** 26 puntos

## DoD — Sprint 4
- GET /catalogo/ → 200 sin autenticación con lista de productos
- Filtrar por categoría → solo productos de esa categoría
- Agregar producto al carrito → contador en navbar se incrementa
- Tarjeta de prueba Stripe 4242... → pedido cambia a "pagado"
- Webhook verifica firma → stock se descuenta
- python manage.py test → ≥ 131 tests OK
