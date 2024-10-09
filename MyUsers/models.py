from django.db import models
from django.utils import timezone

# Create your models here.


class My_User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.created_date}'
