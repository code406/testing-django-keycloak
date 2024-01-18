from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    uuid = models.UUIDField(unique=True)
    realm = models.CharField(max_length=50, default="master")

    preferred_color_scheme = models.CharField(
        max_length=50,
        choices=[("system", "System"), ("light", "Light"), ("dark", "Dark")],
        default="system",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # type: ignore

    def __str__(self) -> str:
        return self.email
