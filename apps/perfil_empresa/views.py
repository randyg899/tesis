from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index_perfil_empresa(request):
    return render(request, "tesis/perfil_empresa.html")
