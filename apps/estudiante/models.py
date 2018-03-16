from django.db import models

from apps.carrera.models import Carrera
# Create your models here.


class Estudiante(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
    cod_alumno = models.IntegerField()
    ciclo = models.CharField(max_length=10)
    telefono = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=100, null=True, blank=True)
    carrera_estudiante = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
