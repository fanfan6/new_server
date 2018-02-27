from django.conf.urls import url, include

from user_info.views import index, index_info
from user_info.views import sex, comp_info
from user_info.views import app_pass, mod_grade, mod_info


urlpatterns = [
    url(r'^index$', index),
    url(r'^index_info$', index_info),
    url(r'^sex$', sex),
    url(r'^comp_info', comp_info),
    url(r'^app_pass', app_pass),
    url(r'^mod_grade', mod_grade),
    url(r'^mod_info', mod_info),
]
