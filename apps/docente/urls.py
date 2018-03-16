from django.conf.urls import url, include

from apps.docente.views import index_docente, docente_view


urlpatterns = [
    url(r'^$', index_docente, name='index'),
    url(r'^nuevo$', docente_view, name='docente_crear'),
]
