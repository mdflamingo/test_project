from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    phone = models.CharField(max_length=12, unique=True)
    confirmation_code = models.CharField("Код подтверждения", blank=True, max_length=150)
    invite_code = models.CharField(max_length=6, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['phone', 'invite_code'],
                                    name='phone_invite_code')]