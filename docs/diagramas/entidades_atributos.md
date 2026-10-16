CATEGORIA (1) ──────────────── (N) PRODUCTO
PROVEEDOR (1) ──────────────── (N) PRODUCTO  (nullable)
CLIENTE   (1) ──────────────── (N) VENTA
CLIENTE   (1) ──────────────── (N) PEDIDO
VENTA     (1) ──────────────── (N) DETALLE_VENTA
PRODUCTO  (1) ──────────────── (N) DETALLE_VENTA

Cardinalidades:
  1:N  → ForeignKey en el lado N
  N:M  → No aplica en este esquema inicial
  1:1  → ConfiguracionERP (singleton: solo 1 fila)