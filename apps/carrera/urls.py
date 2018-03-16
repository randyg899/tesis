from django.conf.urls import url, include

from apps.carrera.views import index_carrera


urlpatterns = [
    url(r'^$', index_carrera),
]
