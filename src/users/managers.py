from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from .keycloak import create_keycloak_user
from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import CustomUser


class CustomUserManager(BaseUserManager["CustomUser"]):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(
        self, email: str, password: str, **extra_fields: Any
    ) -> "CustomUser":
        if not email:
            raise ValueError(_("Users must have an email address"))
        email = self.normalize_email(email)
        username = email
        user = self.model(email=email, username=username, **extra_fields)
        user.uuid = create_keycloak_user(email, password)
        user.save()
        return user

    def create_superuser(
        self, email: str, password: str, **extra_fields: Any
    ) -> "CustomUser":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
