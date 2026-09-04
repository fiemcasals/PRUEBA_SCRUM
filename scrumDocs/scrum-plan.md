# Plan de Requerimientos — projectoPrueba

_Generado automáticamente el 2026-09-04T13:58:34.915Z — no editar a mano, se sobreescribe en cada publicación._

Orden sugerido de desarrollo (respeta dependencias entre Requerimientos). Cada fila indica de qué Requerimientos depende, si tiene.

| Orden | Código | Requerimiento | Historia de Usuario | Módulo | Entrega | Estado | Desarrollador | Depende de | Rechazos |
|---|---|---|---|---|---|---|---|---|---|
| 1 | RF-01 | Servicio y Endpoint de Autenticacion | HU-01 | — | — | Hecho ✓ dev | dev-projectoprueba | — | — |
| 2 | RF-02 | Interfaz de Login y Logout | HU-01 | — | — | production ✓✓ | dev-projectoprueba | — | — |
| 3 | RNF-01 | Seguridad de Credenciales y Manejo de Sesiones | HU-01 | — | — | Hecho ✓ dev | dev-projectoprueba | — | — |
| 4 | RF-01 | API CRUD y Persistencia de Tareas | HU-02 | — | — | Hecho ✓ dev | Sin asignar | — | — |
| 5 | RF-02 | Tablero Visual Kanban Reactivo | HU-02 | — | — | Haciendo | Sin asignar | — | — |
| 6 | RF-01 | Middleware de Control de Acceso basado en Roles (RBAC) | HU-03 | — | — | Haciendo | Sin asignar | — | — |
| 7 | RF-02 | Gestion Administrativa de Usuarios (CRUD y Contrasenas) | HU-03 | — | — | Haciendo | Sin asignar | — | — |
| 8 | RF-01 | Servicio de Registro de Logs de Auditoría | HU-04 | — | — | Haciendo | Sin asignar | — | — |
| 9 | RF-02 | Panel de Visualización y Métricas de Auditoría | HU-04 | — | — | Haciendo | Sin asignar | — | — |

## Detalle

### RF-01 — Servicio y Endpoint de Autenticacion
Implementado servicio y endpoint /api/auth/login con soporte para JWT (access y refresh), autenticación por usuario o email, protección de contraseñas y endpoint /api/auth/me.
- Estimado: 0h

### RF-02 — Interfaz de Login y Logout
Implementado formulario React de Login/Logout con validación de formularios, feedback de error "Credenciales inválidas" y persistencia de token JWT en localStorage/cookies.
- Estimado: 0h

### RNF-01 — Seguridad de Credenciales y Manejo de Sesiones
Implementado hasheo de contraseñas con bcrypt (factor 12), protección de rutas mediante JWT en headers Authorization, y timeout de sesión por inactividad.
- Estimado: 0h

### RF-01 — API CRUD y Persistencia de Tareas
- Estimado: 0h

### RF-02 — Tablero Visual Kanban Reactivo
- Estimado: 0h

### RF-01 — Middleware de Control de Acceso basado en Roles (RBAC)
- Estimado: 0h

### RF-02 — Gestion Administrativa de Usuarios (CRUD y Contrasenas)
- Estimado: 0h

### RF-01 — Servicio de Registro de Logs de Auditoría
- Estimado: 0h

### RF-02 — Panel de Visualización y Métricas de Auditoría
- Estimado: 0h
