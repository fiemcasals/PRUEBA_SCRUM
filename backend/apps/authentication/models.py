from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Administrador'
    USER = 'user', 'Usuario'

class User(AbstractUser):
    email = models.EmailField('Correo electrónico', unique=True)
    role = models.CharField(
        'Rol',
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_admin_role(self):
        return self.role == UserRole.ADMIN or self.is_superuser
