from rest_framework import generics
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

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
