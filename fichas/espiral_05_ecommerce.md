# Ficha de Sistematización — Espiral 5
## ERP Django · Espiral E5: E-commerce y Pagos

| Campo | Contenido |
|---|---|
| **Número de espiral** | 5 |
| **Nombre del ciclo** | E-commerce y Pagos |
| **Semanas** | W13 – W15 |
| **Fecha de inicio** | ___/___/_____ |
| **Fecha de cierre** | 22/11/2026 |
| **Responsable** | [Nombre del estudiante] |
| **Asesor** | MC. Román Fernando López González |

## 1. Objetivo del ciclo
Implementar el canal de e-commerce completo: catálogo público filtrable,
carrito de compras en sesión, proceso de pago con Stripe y confirmación
automática vía webhook con descuento de stock.

## 2. Tareas realizadas

| # | Tarea | Estado | Semana |
|---|---|---|---|
| 1 | App catalogo + django-filter | ✅ | W13 |
| 2 | CatalogoView pública con filtros | ✅ | W13 |
| 3 | Carrito en sesión (5 vistas) | ✅ | W13 |
| 4 | Context processor carrito_info | ✅ | W13 |
| 5 | Templates catálogo + carrito | ✅ | W13 |
| 6 | pip install stripe | ✅ | W14 |
| 7 | CheckoutView con PaymentIntent | ✅ | W14 |
| 8 | Template checkout.html con Stripe.js | ✅ | W14 |
| 9 | pago_exitoso + pago_error | ✅ | W14 |
| 10 | items_snapshot en Pedido + migración 0003 | ✅ | W15 |
| 11 | Webhook endpoint con verificación de firma | ✅ | W15 |
| 12 | Descuento de stock con F() | ✅ | W15 |
| 13 | Tests con mock (Stripe + webhook) | ✅ | W15 |

## 3. Evidencias
- URL catálogo: https://erp-django-utec-5b9p.onrender.com/catalogo/
- Webhook Stripe configurado en el Dashboard (sandbox) con destino "Render"
  → https://erp-django-utec-5b9p.onrender.com/catalogo/webhook/
- Stripe CLI usada en local (`stripe listen`) → `[200]` en
  `payment_intent.succeeded`
- Tests: Ran 147 tests → OK
- Pedido 'pendiente' → 'pagado' via webhook verificado en /admin/
  (local y Render)
- Stock decrementado verificado en /admin/productos/

## 4. Criterios de aceptación

| Criterio | Estado |
|---|---|
| GET /catalogo/ sin auth → 200 | ✅ |
| Filtro por nombre/categoría/precio | ✅ |
| Agregar/remover/actualizar carrito | ✅ |
| Tarjeta 4242 → pago exitoso | ✅ |
| Webhook payment_intent.succeeded → Pedido 'pagado' | ✅ |
| Stock decrementado con F() (atómico) | ✅ |
| Firma inválida → 400 | ✅ |
| 147 tests OK | ✅ |

## 5. Problemas encontrados
1. **`stripe listen` pedía eventos.** La versión 1.55 de la Stripe CLI
   exige `--events` (o `--all-snapshot`); la guía no lo incluía.
   *Solución:* `stripe listen --events payment_intent.succeeded,payment_intent.payment_failed --forward-to http://127.0.0.1:8000/catalogo/webhook/`
2. **Confusión entre cuentas de Stripe.** El login de la CLI ofrece cuenta
   activa (datos reales) y entornos de prueba. *Solución:* autorizar solo
   el entorno de prueba (sandbox) que corresponde a las claves `pk_test_`
   / `sk_test_` del proyecto.
3. **URL de Render.** La guía usa un marcador (`TU-URL`); hay que usar la
   URL real del servicio. *Solución:* copiarla de Render y verificarla con
   un GET (responde 405).
4. **Secretos de webhook distintos.** El `whsec_` de la CLI solo sirve en
   local; en Render se usa el *Signing secret* del destino del Dashboard.
5. **Error de commit.** Se escribió un mensaje de commit equivocado antes
   del push. *Solución:* `git commit --amend -m "..."` (válido porque aún
   no se había hecho push).

## 6. Lecciones aprendidas
1. El webhook es la fuente de verdad del estado del pago: confirma el
   pedido aunque el usuario cierre el navegador.
2. Verificar la firma del webhook es lo que impide que un atacante marque
   pedidos como pagados.
3. Local y producción usan configuraciones distintas (CLI vs. Dashboard,
   dos `STRIPE_WEBHOOK_SECRET`): conviene probar ambos por separado.
4. Un mock debe parecerse al objeto real; con librerías que cambian de
   versión, los tests con `dict` simples pueden pasar aunque falle producción.

## 7. Tiempo total invertido

| Categoría | Horas |
|---|---|
| Diseño | |
| Implementación | |
| Pruebas | |
| Documentación | |
| **Total Espiral 5** | |
