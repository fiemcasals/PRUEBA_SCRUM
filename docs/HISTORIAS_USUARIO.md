# Historias de Usuario -- projectoPrueba

_Generado automaticamente el 2026-08-12T15:20:40.163Z -- no editar a mano, se sobreescribe en cada publicacion._

## HU-01: Inicio de Sesión y Autenticación de Usuarios

Como usuario del sistema, quiero iniciar sesión con mi correo/usuario y contraseña para acceder de manera segura a mi espacio de trabajo según mis permisos.

### Criterios de Aceptacion

- Existe un formulario de login con campos para usuario/email y contraseña.
- Al ingresar credenciales válidas, el usuario es redirigido al Dashboard (o al panel de Admin si corresponde).
- Si las credenciales son incorrectas, se muestra un mensaje de error claro y genérico ("Credenciales inválidas").
- El sistema mantiene la sesión activa mientras el usuario navega.
- Existe un botón o acción visible para Cerrar Sesión (Logout) que invalida la sesión y redirige al login.

### Detalle Tecnico y Reglas de Negocio

Autenticación basada en sesiones seguras / tokens JWT con almacenamiento de contraseñas hasheadas (bcrypt/argon2).
