# Sprint 3 Planning — ERP Django
## Semanas W10–W12 · Espiral 4: API REST y Media

**Sprint Goal:**
Al finalizar el Sprint 3, el ERP expondrá una API REST completa
con autenticación por token, gestión de imágenes de productos
y generación de PDFs de facturas.

## Sprint Backlog — actualización W10

| Tarea | Estado |
|---|---|
| rest_framework.authtoken instalado | ✅ W10 |
| Serializers × 5 entidades | ✅ W10 |
| ListCreateAPIView + RetrieveUpdateDestroyAPIView × 5 | ✅ W10 |
| api_urls.py × 4 apps + /api/ en core/urls.py | ✅ W10 |
| Token endpoint /api/auth/token/ | ✅ W10 |
| 7 tests APIClient pasando | ✅ W10 |
| ImageField + Pillow + MEDIA_ROOT | ⏳ W11 |
| django-storages + S3/MinIO | ⏳ W11 |
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