# Historias de Usuario -- projectoPrueba

_Generado automaticamente el 2026-08-13T16:20:05.480Z -- no editar a mano, se sobreescribe en cada publicacion._

## HU-01: Inicio de Sesión y Autenticación de Usuarios (Actualizado)

Como usuario del sistema, quiero iniciar sesión con mi correo/usuario y contraseña para acceder de manera segura a mi espacio de trabajo.

### Criterios de Aceptacion

- Formulario de login
- Validación JWT
- Logout con invalidación de sesión
- Manejo de errores genéricos

### Detalle Tecnico y Reglas de Negocio

Autenticación con JWT (access/refresh token) y bcrypt con factor >= 10.

## HU-02: Tablero Kanban de Tareas (Dashboard)

Como miembro del equipo autenticado, quiero visualizar y gestionar tareas en un tablero con columnas To Do, Doing y Done para hacer seguimiento del estado y avance del trabajo de forma ágil.

### Criterios de Aceptacion

- El Dashboard muestra 3 columnas principales: To Do, Doing y Done.
- Se pueden crear nuevas tareas indicando al menos un título y una descripción (por defecto entran en To Do).
- Las tarjetas de tareas se pueden mover entre columnas (cambio de estado).
- El cambio de estado se persiste automáticamente en la base de datos.
- Cada tarjeta muestra claramente su información básica (título, descripción breve y estado).

### Detalle Tecnico y Reglas de Negocio

Componente de tablero Kanban reactivo con persistencia de estado de tareas en base de datos.

## HU-03: Panel de Administración y Gestión de Usuarios

Como Administrador del sistema, quiero crear nuevos usuarios y gestionar sus contraseñas y accesos para controlar quién puede ingresar al sistema y administrar el equipo.

### Criterios de Aceptacion

- La vista de administración es accesible únicamente para usuarios con rol Admin (los demás usuarios reciben acceso denegado o son redirigidos al Dashboard).
- Permite listar todos los usuarios registrados en el sistema.
- Permite crear nuevos usuarios completando nombre, email, rol (Usuario / Admin) y contraseña inicial.
- Permite restablecer o cambiar la contraseña de un usuario existente.
- Permite editar datos de usuario o deshabilitar/eliminar cuentas.

### Detalle Tecnico y Reglas de Negocio

Rutas protegidas por middleware de roles (RBAC) y endpoints CRUD para administración de usuarios.

## HU-04: HU-04: Notificaciones y Auditoría de Actividad

Como Administrador del sistema, quiero registrar y consultar el historial de auditoría de inicio de sesión y acciones críticas para monitorear la seguridad.

### Criterios de Aceptacion

- Registro de logs de login
- Notificación de accesos sospechosos
- Visualización de logs para Admin

### Detalle Tecnico y Reglas de Negocio

Tabla de logs de auditoría indexada por timestamp y usuario.
