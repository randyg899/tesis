from django.db import models
from apps.estudiante.models import Estudiante
# Create your models here.


class PerfilEstudiante(models.Model):
    conocimientos = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    estudiante_perfil = models.ForeignKey(Estudiante,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Perfil: {}'.format(self.estudiante_perfil)
