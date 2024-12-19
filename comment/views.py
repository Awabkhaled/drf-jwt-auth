from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CommentViewSet(ModelViewSet):
    """An endpoint to handle comments operations"""
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    queryset = Comment.objects.all()

    def get_queryset(self):
        """Return comments for the authenticated user."""
        return Comment.objects.filter(user=self.request.user)
