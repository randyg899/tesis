from django.db import models

from apps.especialidad.models import Especialidad
# Create your models here.


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    ciclos = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    especialidad_carrera = models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
