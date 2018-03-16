from django.db import models

# Create your models here.


class Empresa(models.Model):
    nombre = models.CharField(max_length=70)
    ruc = models.IntegerField()
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)
    rubro = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.nombre)
