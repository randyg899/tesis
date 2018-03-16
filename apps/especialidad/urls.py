from django.conf.urls import url, include

from apps.especialidad.views import index_especialidad


urlpatterns = [
    url(r'^$', index_especialidad),
]
