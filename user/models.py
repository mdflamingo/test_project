from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class User(AbstractUser):
    """Модель пользователя."""

    phone_number = models.CharField(max_length=12, unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def send_sms(self, message, **kwargs):
        if User.objects.filter(phone_number=self.phone_number).exists():
            # If the phone_number already exists, send the SMS
            print(f'Sending SMS message to {self.phone_number}: {message}')
        else:
            # If the phone_number does not exist, raise an error
            raise ValueError('The phone number does not exist in the system.')