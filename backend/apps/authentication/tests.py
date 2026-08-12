from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, UserRole

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.password = 'SecurePass123!'
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password=self.password,
            first_name='Test',
            last_name='User',
            role=UserRole.USER
        )
        self.admin_user = User.objects.create_user(
            username='adminuser',
            email='admin@example.com',
            password=self.password,
            first_name='Admin',
            last_name='User',
            role=UserRole.ADMIN,
            is_staff=True
        )

    def test_login_success_with_username(self):
        """Test login with valid username and password."""
        url = reverse('auth_login')
        data = {
            'username': 'testuser',
            'password': self.password
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')
        self.assertEqual(response.data['user']['email'], 'testuser@example.com')

    def test_login_success_with_email(self):
        """Test login with valid email and password."""
        url = reverse('auth_login')
        data = {
            'email': 'testuser@example.com',
            'password': self.password
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')

    def test_login_invalid_password(self):
        """Test login with invalid password returns 401."""
        url = reverse('auth_login')
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Credenciales inválidas')

    def test_login_nonexistent_user(self):
        """Test login with nonexistent user returns 401."""
        url = reverse('auth_login')
        data = {
            'username': 'nonexistent',
            'password': 'password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Credenciales inválidas')

    def test_me_endpoint_authenticated(self):
        """Test /api/auth/me with JWT token returns user details."""
        # First login
        login_url = reverse('auth_login')
        login_resp = self.client.post(login_url, {
            'username': 'testuser',
            'password': self.password
        }, format='json')
        token = login_resp.data['access']

        # Call /api/auth/me with Bearer token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        me_url = reverse('auth_me')
        response = self.client.get(me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['role'], 'user')

    def test_me_endpoint_unauthenticated(self):
        """Test /api/auth/me without token returns 401."""
        me_url = reverse('auth_me')
        response = self.client.get(me_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
