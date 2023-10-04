from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cookies = models.JSONField(default=dict)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'