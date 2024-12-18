from django.urls import path, include
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter
app_name = 'comment'
router = DefaultRouter()
router.register('', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
