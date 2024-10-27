from django.db import models


class OTPType(models.IntegerChoices):
    REGISTER = 0, 'Регистрация'
    RESET_PASSWORD = 1, 'Восстановить пароль'
