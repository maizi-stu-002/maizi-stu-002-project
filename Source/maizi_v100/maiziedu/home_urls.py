from django.conf.urls import include, url
from django.contrib import admin
from maiziedu.home_views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
]
