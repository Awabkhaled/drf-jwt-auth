from rest_framework import generics
from .serializers import UserSerializer, UserLogOutSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateUser(generics.CreateAPIView):
    """An end point for creating users with name and password"""
    serializer_class = UserSerializer


class UpdateRetrieveUser(generics.RetrieveUpdateAPIView):
    """An endpoint for updating and retrieving users"""
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class Logout(APIView):
    """An endpoint to logout a user"""
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = UserLogOutSerializer(
            data=request.data, context={'access_token': request.auth})
        serializer.is_valid(raise_exception=True)
        refresh_token_string = serializer.validated_data['refresh']
        try:
            refresh_token = RefreshToken(refresh_token_string)
            refresh_token.blacklist()
            return Response({'message': 'Successfully logged out'}, status=200)
        except Exception:
            return Response({'error': 'Failed to blacklist token'}, status=400)
