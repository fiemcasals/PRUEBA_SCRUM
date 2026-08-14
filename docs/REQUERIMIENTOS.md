# Requerimientos -- projectoPrueba

_Generado automaticamente el 2026-08-14T13:33:11.324Z -- no editar a mano, se sobreescribe en cada publicacion._

## HU-01: HU-01: Inicio de Sesión y Autenticación de Usuarios

### RF-01: Servicio y Endpoint de Autenticacion (Funcional)

Endpoint /api/auth/login que valida usuario/email y contrasena, verifica el hash de seguridad y retorna token JWT o cookie de sesion valida.

### RF-02: Interfaz de Login y Logout (Funcional)

Formulario web con validaciones de campos, visualizacion de errores genericos ('Credenciales invalidas'), persistencia de estado de sesion y boton de cierre de sesion (Logout) con redireccion.

### RNF-01: Seguridad de Credenciales y Manejo de Sesiones (No funcional)

Hasheo seguro de contrasenas con salting (bcrypt con factor >= 10 o Argon2id) y expiracion de tokens/sesiones por inactividad.

## HU-02: HU-02: Tablero Kanban de Tareas (Dashboard)

### RF-01: API CRUD y Persistencia de Tareas (Funcional)

Endpoints REST para listar tareas, crear nueva tarea con titulo y descripcion (ingreso inicial en To Do) y actualizar su estado o contenido en la base de datos.

### RF-02: Tablero Visual Kanban Reactivo (Funcional)

Vista de Dashboard con 3 columnas (To Do, Doing, Done), tarjetas informativas de cada tarea y soporte para moverlas de columna persistiendo el nuevo estado en tiempo real.

## HU-03: HU-03: Panel de Administración y Gestión de Usuarios

### RF-01: Middleware de Control de Acceso basado en Roles (RBAC) (Funcional)

Proteccion de rutas a nivel backend y frontend para restringir el acceso al panel administrativo exclusivamente a usuarios con rol Admin.

### RF-02: Gestion Administrativa de Usuarios (CRUD y Contrasenas) (Funcional)

Interfaz y endpoints para listar usuarios del sistema, crear nuevos usuarios (nombre, email, rol, clave inicial), editar datos, resetear contrasenas y dar de baja cuentas.

## HU-04: HU-04: Auditoría de Seguridad y Registro de Eventos

### RF-01: Servicio de Registro de Logs de Auditoría (Funcional)

Middleware para registrar eventos de login y acciones administrativas en base de datos.

### RF-02: Panel de Visualización y Métricas de Auditoría (Funcional)

Vista administrativa y endpoints para filtrar y exportar logs de actividad del sistema.
