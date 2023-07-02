from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class CustomUser(AbstractUser):

    objects = CustomUserManager()

    phone = models.IntegerField(null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

