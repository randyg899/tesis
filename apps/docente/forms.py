from django import forms

from apps.docente.models import Docente


class Docenteform(forms.ModelForm):
    class Meta:
        model = Docente

        fields = [
            'nombres',
            'apellidos',
            'dni',
            'telefono',
            'email',
            'grado',
        ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'dni': 'D.N.I:',
            'telefono': 'Celular',
            'email': 'Correo',
            'grado': 'Grado Academico',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.TextInput(attrs={'class': 'form-control'}),
        }
