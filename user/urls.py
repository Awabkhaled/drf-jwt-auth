from django.urls import path
from .views import (
  CreateUser,
  UpdateRetrieveUser,
  Logout,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('signup/', CreateUser.as_view(), name="create"),
    path('update_get/', UpdateRetrieveUser.as_view(), name="update_get"),
    path('logout/', Logout.as_view(), name='Logout'),
]
