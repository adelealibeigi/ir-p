from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    from user.managers import CustomUserManager

    phone_number_regex = RegexValidator(regex=r'^(\+98|98|0)?(9\d{9})$', message='Enter a valid phone number.')
    phone_number = models.CharField('PhoneNumber', unique=True, max_length=15, validators=[phone_number_regex])
    full_name = models.CharField(db_column='FullName', max_length=100)
    username = None
    # REQUIRED_FIELDS = [phone_number]
    USERNAME_FIELD = 'phone_number'
    created = models.DateTimeField('Created', auto_now=True)
    updated = models.DateTimeField('Updated', auto_now_add=True)
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.id} {self.password}'
