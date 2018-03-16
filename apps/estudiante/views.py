from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.estudiante.forms import Estudianteform


# Create your views here.


def index_estudiante(request):
    return render(request, "tesis/estudiante.html")


def estudiante_view(request):
    if request.method == 'POST':
        form = Estudianteform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Estudiante:index')
    else:
        form = Estudianteform()

    return render(request, 'tesis/estudiante_form.html', {'form': form})
