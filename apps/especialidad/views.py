from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index_especialidad(request):
    return render(request, "tesis/especialidad.html")
