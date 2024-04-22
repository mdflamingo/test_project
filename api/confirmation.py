import time
import random
from user.models import User


def generate_authorization_code() -> str:
    """Функция для генерации 4х значного кода подтверждения."""

    time.sleep(random.uniform(1, 2))
    code = str(random.randint(1000, 9999))
    print(code)
    return code


def send_confirmation_code(user: User) -> str:
    """Функция для отправки кода подтверждения."""

    confirmation_code = generate_authorization_code()
    user.send_sms(confirmation_code)
    return confirmation_code
