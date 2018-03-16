from django.conf.urls import url, include

from apps.perfil_empresa.views import index_perfil_empresa


urlpatterns = [
    url(r'^$', index_perfil_empresa),
]
