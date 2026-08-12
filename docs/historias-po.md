# Historias de Usuario - projectoPrueba

## HU-01: Inicio de Sesión y Autenticación de Usuarios
**Descripción:**
Como usuario del sistema, quiero iniciar sesión con mi correo/usuario y contraseña para acceder de manera segura a mi espacio de trabajo según mis permisos.

**Criterios de Aceptación:**
- Existe un formulario de login con campos para usuario/email y contraseña.
- Al ingresar credenciales válidas, el usuario es redirigido al Dashboard (o al panel de Admin si corresponde).
- Si las credenciales son incorrectas, se muestra un mensaje de error claro y genérico ("Credenciales inválidas").
- El sistema mantiene la sesión activa mientras el usuario navega.
- Existe un botón o acción visible para Cerrar Sesión (Logout) que invalida la sesión y redirige al login.

**Detalle Técnico:**
Autenticación basada en sesiones seguras / tokens JWT con almacenamiento de contraseñas hasheadas (bcrypt/argon2).

---

## HU-02: Tablero Kanban de Tareas (Dashboard)
**Descripción:**
Como miembro del equipo autenticado, quiero visualizar y gestionar tareas en un tablero con columnas To Do, Doing y Done para hacer seguimiento del estado y avance del trabajo de forma ágil.

**Criterios de Aceptación:**
- El Dashboard muestra 3 columnas principales: To Do, Doing y Done.
- Se pueden crear nuevas tareas indicando al menos un título y una descripción (por defecto entran en To Do).
- Las tarjetas de tareas se pueden mover entre columnas (cambio de estado).
- El cambio de estado se persiste automáticamente en la base de datos.
- Cada tarjeta muestra claramente su información básica (título, descripción breve y estado).

**Detalle Técnico:**
Componente de tablero Kanban reactivo con persistencia de estado de tareas en base de datos.

---

## HU-03: Panel de Administración y Gestión de Usuarios
**Descripción:**
Como Administrador del sistema, quiero crear nuevos usuarios y gestionar sus contraseñas y accesos para controlar quién puede ingresar al sistema y administrar el equipo.

**Criterios de Aceptación:**
- La vista de administración es accesible únicamente para usuarios con rol Admin (los demás usuarios reciben acceso denegado o son redirigidos al Dashboard).
- Permite listar todos los usuarios registrados en el sistema.
- Permite crear nuevos usuarios completando nombre, email, rol (Usuario / Admin) y contraseña inicial.
- Permite restablecer o cambiar la contraseña de un usuario existente.
- Permite editar datos de usuario o deshabilitar/eliminar cuentas.

**Detalle Técnico:**
Rutas protegidas por middleware de roles (RBAC) y endpoints CRUD para administración de usuarios.
