from django.urls import path
from .views import (
  CreateUser,
  UpdateRetrieveUser
)

urlpatterns = [
    path('signup/', CreateUser.as_view(), name="create"),
    path('update_get/', UpdateRetrieveUser.as_view(), name="update_get"),
]
