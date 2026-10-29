# Sprint 2 Planning — ERP Django
## Semanas W07–W09 · Espiral 3: CRUD Web y Autenticación

**Sprint Goal:**
Al finalizar el Sprint 2, el ERP mostrará lista y detalle de las
entidades principales, con formularios de alta/edición/borrado
protegidos por autenticación y 3 roles de acceso.

**Duración:** W07 (ListView/DetailView) · W08 (CreateView/UpdateView/DeleteView) · W09 (Auth+RBAC · M3)

## Sprint 2 — Estado final W09

| HU | Estado | Pts |
|---|---|---|
| HU-E3-01 a HU-E3-09 | ✅ Completadas | 27/27 |

## Hito M3 — ALCANZADO ✅
- CRUD: 4 módulos con lectura + escritura funcional
- Auth: allauth con login/logout Fable 5
- RBAC: 3 grupos (Gerente/Vendedor/Almacén) con permisos
- Tests: Ran 100 tests → OK
- Fecha: ___/___/_____

## DoD — Sprint 2
- ListView responde HTTP 200 y muestra objetos de la BD
- DetailView responde 200 con datos correctos y 404 para IDs inexistentes
- Formularios de escritura requieren login (redirigen a `/accounts/login/`)
- 3 grupos Django (Gerente, Vendedor, Almacén) con permisos asignados
- python manage.py test tests → ≥ 78 tests OK