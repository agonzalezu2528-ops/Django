# Sprint 3 Planning — ERP Django
## Semanas W10–W12 · Espiral 4: API REST y Media

**Sprint Goal:**
Al finalizar el Sprint 3, el ERP expondrá una API REST completa
con autenticación por token, gestión de imágenes de productos
y generación de PDFs de facturas.

## Sprint Backlog — actualización W11

| Tarea | Estado |
|---|---|
| Serializers + API Views + Token Auth | ✅ W10 |
| Pillow + filetype instalados | ✅ W11 |
| ImageField en Producto + migración 0002 | ✅ W11 |
| Validador custom (MIME + tamaño) | ✅ W11 |
| ProductoSerializer con imagen_url | ✅ W11 |
| ProductoForm con widget imagen | ✅ W11 |
| Templates crear/editar: enctype multipart | ✅ W11 |
| detalle.html muestra imagen | ✅ W11 |
| ProductoAdmin con preview de imagen | ✅ W11 |
| django-storages configurado para prod | ✅ W11 |
| 8 tests de media pasando | ✅ W11 |
| Generación PDF WeasyPrint | ⏳ W12 |
| Exportación Excel openpyxl | ⏳ W12 |

**Total Sprint 3:** 21 puntos

## DoD — Sprint 3
- GET /api/productos/ → JSON 200 sin autenticación
- POST /api/productos/ sin token → 403
- POST /api/productos/ con token válido → 201
- Imagen de producto visible en /media/
- GET /ventas/<id>/pdf/ → descarga PDF con líneas de detalle
- GET /productos/exportar-excel/ → archivo .xlsx descargable
- python manage.py test tests → ≥ 107 tests OK

