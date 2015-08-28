#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from maiziedu.home_views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^hascourse/(\d+)$', has_course, name='has-course'),  # 教师课程详情页
    url(r'^searchresults/$', search_results, name='search-results'),  # 搜索结果
]
