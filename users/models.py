from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)


class Rules(models.Model):
    article = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return f"{self.article}"
