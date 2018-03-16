from django.conf.urls import url, include

from apps.estudiante.views import index_estudiante, estudiante_view


urlpatterns = [
    url(r'^$', index_estudiante, name='index'),
    url(r'^nuevo$', estudiante_view, name='estudiante_crear'),
]
