from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    objects = CustomUserManager()
    username = models.CharField(max_length=225, unique=True)
    email = models
    phone = models.IntegerField(null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'