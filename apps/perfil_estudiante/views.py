from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.perfil_estudiante.forms import Perfil_Estudiante_form

# Create your views here.


def index_perfil_estudiante(request):
    return render(request, "tesis/perfil_estudiante.html")


def perfil_estudiante_view(request):
    if request.method == 'POST':
        form = Perfil_Estudiante_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('PerfilEstudiante:index')
    else:
        form = Perfil_Estudiante_form()

    return render(request, 'tesis/perfil_estudiante_form.html', {'form': form})
