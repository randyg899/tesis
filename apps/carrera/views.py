from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index_carrera(request):
    return render(request, "tesis/carrera.html")
