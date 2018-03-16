from django.conf.urls import url, include

from apps.perfil_estudiante.views import index_perfil_estudiante, perfil_estudiante_view


urlpatterns = [
    url(r'^$', index_perfil_estudiante, name='index'),
    url(r'^nuevo$', perfil_estudiante_view, name='Perfil_crear'),
]
