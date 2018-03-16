from django.conf.urls import url, include

from apps.empresa.views import index_empresa


urlpatterns = [
    url(r'^$', index_empresa),
]
