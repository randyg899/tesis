from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.docente.forms import Docenteform


# Create your views here.


def index_docente(request):
    return render(request, "tesis/docente.html")


def docente_view(request):
    if request.method == 'POST':
        form = Docenteform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Docente:index')
    else:
        form = Docenteform()

    return render(request, 'tesis/docente_form.html', {'form': form})
