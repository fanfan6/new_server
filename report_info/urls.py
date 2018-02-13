from django.conf.urls import url, include

from report_info import views


urlpatterns = [
    url(r'^report/(?P<nid>\d+)', views.report),
<<<<<<< HEAD
    url(r'^service_info$', views.service_info),
    url(r'^search$', views.search),
    url(r'^search_info$', views.search_info),
    url(r'^downpdf$', views.downpdf),
    url(r'^history$', views.report_history),
=======
    url(r'^service$', views.service),
    url(r'^search$', views.search),
    url(r'^search_info$', views.search_info),
>>>>>>> 710c2c4130860b16d58fd9df0822ab73623f8a44
]
