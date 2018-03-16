from django import forms

from apps.estudiante.models import Estudiante


class Estudianteform(forms.ModelForm):
    class Meta:
        model = Estudiante

        fields = [
            'nombres',
            'apellidos',
            'fecha_nacimiento',
            'dni',
            'cod_alumno',
            'ciclo',
            'telefono',
            'email',
            'direccion',
            'carrera_estudiante',
        ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'dni': 'D.N.I.',
            'cod_alumno': 'Codigo de Alumno',
            'ciclo': 'Ciclo Academico',
            'telefono': 'Celular',
            'email': 'Correo',
            'direccion': 'Dirección',
            'carrera_estudiante': 'Carrera Profesional',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_alumno': forms.TextInput(attrs={'class': 'form-control'}),
            'ciclo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera_estudiante': forms.RadioSelect(),
        }
