from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """User manager to manage the Custom `User` class"""
    def create_user(self, name, password, **extrafields):
        """Custom Creating User with the name field"""
        if not name:
            raise ValueError("The Name is required")
        user = self.model(name=name, **extrafields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, name, password, **extrafields):
        """Custom Creating User with the name field"""
        user = self.create_user(name, password, **extrafields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User Table Using the default behavior of `AbstractBaseUser`"""
    name = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'name'
