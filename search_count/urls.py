from django.conf.urls import url, include

from search_count.views import count_info, counts, count_download


urlpatterns = [
    url(r'^count_info?.*$', count_info),
    url(r'^search$', counts),
    url(r'^download$', count_download),
]
