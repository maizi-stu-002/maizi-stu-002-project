from django.conf.urls import url
from maiziedu.home_views import *

urlpatterns = [
    url(r'^$', index, name='index'),
]
