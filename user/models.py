from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    phone_number = models.CharField(max_length=12)
    username = models.CharField('Username', max_length=150, unique=True)
    # confirmation_code = models.CharField('Confirmation Code', blank=True, max_length=150)
    invite_code = models.CharField(max_length=6, blank=True)
    # is_verifide = models.BooleanField('Verified', default=False)

    # USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = ['username']

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['phone_number', 'invite_code'],
    #                                 name='phone_invite_code')]

    def send_sms(self, message, **kwargs):
        print(f'Sending SMS message to {self.phone_number}: {message}')

