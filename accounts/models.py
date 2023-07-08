from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
import random

class OTP(models.Model):
    code = models.SmallIntegerField(default=random.randrange(1000, 9999))
    date = models.DateTimeField(auto_now=True)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    username = models.CharField(max_length=225, unique=True)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    otp = models.ForeignKey(OTP, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    is_confirm = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
