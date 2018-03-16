from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index_empresa(request):
    return render(request, "tesis/empresa.html")
