from django.db import models

# Create your models here.


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.nombre)
