# Sprint 2 Planning — ERP Django
## Semanas W07–W09 · Espiral 3: CRUD Web y Autenticación

**Sprint Goal:**
Al finalizar el Sprint 2, el ERP mostrará lista y detalle de las
entidades principales, con formularios de alta/edición/borrado
protegidos por autenticación y 3 roles de acceso.

**Duración:** W07 (ListView/DetailView) · W08 (CreateView/UpdateView/DeleteView) · W09 (Auth+RBAC · M3)

## Sprint Backlog — actualización W07

| Tarea | Estado |
|---|---|
| ListView + DetailView para 4 apps | ✅ W07 |
| 8 templates lista.html + detalle.html | ✅ W07 |
| urls.py con rutas lista y detalle | ✅ W07 |
| select_related/prefetch_related anti N+1 | ✅ W07 |
| 12 tests de vistas de lectura | ✅ W07 |
| CreateView + UpdateView + DeleteView | ⏳ W08 |
| Login/Logout + LoginRequiredMixin | ⏳ W09 |
| 3 roles RBAC | ⏳ W09 |

**Total Sprint 2:** 27 puntos

## DoD — Sprint 2
- ListView responde HTTP 200 y muestra objetos de la BD
- DetailView responde 200 con datos correctos y 404 para IDs inexistentes
- Formularios de escritura requieren login (redirigen a `/accounts/login/`)
- 3 grupos Django (Gerente, Vendedor, Almacén) con permisos asignados
- python manage.py test tests → ≥ 78 tests OK