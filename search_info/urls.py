from django.conf.urls import url, include

from search_info.views import search, search_info


urlpatterns = [
    # url(r'^report/(?P<nid>\d+)', views.report),
    # url(r'^service_info$', views.service_info),
    # url(r'^service_user$', views.service_user),
    url(r'^search$', search),
    url(r'^search_info$', search_info),
    # url(r'^history$', views.report_history),
]
