from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ...


class Producto(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.year} - {self.year}"



