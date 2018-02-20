from django.conf.urls import url, include

from search_info.views import search, search_info
from search_info.views import service, service_info
from search_info.views import history, report


urlpatterns = [
    url(r'^report/(?P<nid>\d+)', report),
    url(r'^service_info$', service_info),
    url(r'^service$', service),
    url(r'^search$', search),
    url(r'^search_info$', search_info),
    url(r'^history$', history),
]
