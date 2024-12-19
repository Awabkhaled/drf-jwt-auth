from django.urls import path
from .views import (
  CreateUser,
  UpdateRetrieveUser,
  Logout,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenObtainSlidingView,
    TokenRefreshSlidingView
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('signup/', CreateUser.as_view(), name="create"),
    path('update_get/', UpdateRetrieveUser.as_view(), name="update_get"),
    path('logout/', Logout.as_view(), name='Logout'),
    path('sliding-login/', TokenObtainSlidingView.as_view(),
         name='sliding_token_obtain'),
    path('sliding-login/refresh/', TokenRefreshSlidingView.as_view(),
         name='sliding_token_refresh'),
]
