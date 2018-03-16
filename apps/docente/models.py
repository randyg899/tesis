from django.db import models

# Create your models here.


class Docente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    grado = models.CharField(max_length=20)

    def __str__(self):
        return '{} {} {}'.format(self.grado, self.nombres, self.apellidos)
