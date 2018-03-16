from django.db import models
from apps.empresa.models import Empresa

# Create your models here.


class PerfilEmpresa(models.Model):
    empresa_perfil = models.ForeignKey(Empresa,null=True, blank=True, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=30)
    remuneracion = models.IntegerField(null=True, blank=True)
    conocimientos_deseados = models.CharField(max_length=300)
    horario_trabajo = models.CharField(max_length=100)
    telefono_contacto = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return 'Perfil de {}'.format(self.empresa_perfil)
