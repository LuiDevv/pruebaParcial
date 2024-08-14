from django.db import models

# Create your models here.

from django.db import models

class Producto(models.Model):
    codigoProducto = models.CharField(max_length=100)
    descripcionProducto = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigoProducto} - {self.descripcionProducto}"



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)



