from rest_framework import generics
from .serializers import UserSerializer

class CreateUser(generics.CreateAPIView):
    """An end point for creating users with name and password"""
    serializer_class = UserSerializer

class UpdateRetrieveUser(generics.RetrieveUpdateAPIView):
    """An endpoint for updating and retrieving users"""
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


