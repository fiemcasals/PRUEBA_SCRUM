from django.core.management.base import BaseCommand
from apps.authentication.models import User, UserRole

class Command(BaseCommand):
    help = 'Seeds initial test users for development'

    def handle(self, *args, **options):
        # Admin user
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@proyecto.local',
                password='AdminPassword123!',
                first_name='Admin',
                last_name='Sistema',
                role=UserRole.ADMIN
            )
            self.stdout.write(self.style.SUCCESS(f'Created admin user: {admin.username} / AdminPassword123!'))

        # Standard user
        if not User.objects.filter(username='usuario').exists():
            user = User.objects.create_user(
                username='usuario',
                email='usuario@proyecto.local',
                password='UserPassword123!',
                first_name='Usuario',
                last_name='Prueba',
                role=UserRole.USER
            )
            self.stdout.write(self.style.SUCCESS(f'Created regular user: {user.username} / UserPassword123!'))
