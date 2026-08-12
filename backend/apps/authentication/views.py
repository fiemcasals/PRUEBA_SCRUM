from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, UserSerializer, UserCreateSerializer
from .models import User

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            access_token = serializer.validated_data['access']
            refresh_token = serializer.validated_data['refresh']

            return Response({
                'message': 'Autenticación exitosa',
                'access': access_token,
                'refresh': refresh_token,
                'token': access_token, # alias compatibility
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)

        # Generic clear error message for security
        error_msg = 'Credenciales inválidas'
        if 'non_field_errors' in serializer.errors:
            error_msg = serializer.errors['non_field_errors'][0]

        return Response({
            'error': error_msg,
            'details': serializer.errors
        }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'Sesión cerrada'}, status=status.HTTP_200_OK)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
