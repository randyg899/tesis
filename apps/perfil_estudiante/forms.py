from django import forms

from apps.perfil_estudiante.models import PerfilEstudiante


class Perfil_Estudiante_form(forms.ModelForm):
    class Meta:
        model = PerfilEstudiante

        fields = [
            'estudiante_perfil',
            'conocimientos',
            'descripcion',
        ]
        labels = {
            'estudiante_perfil': 'Estudiante',
            'conocimientos': 'Lista de Conocimientos',
            'descripcion': 'Breve Descripcion',
        }
        widgets = {
            'estudiante_perfil': forms.RadioSelect(),
            'conocimientos': forms.TextInput(attrs={'class': 'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
