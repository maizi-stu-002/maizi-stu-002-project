#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.shortcuts import render

logger = logging.getLogger('maiziedu.home_views')


# 全局信息
def global_setting(request):
    pass


# 首页
def index(request):
    try:
        return render(request, 'home/index.html', locals())
    except Exception as e:
        logger.error(e)


# 广告
def ad(request):
    pass


# 搜索
def search_command(request):
    pass


# 课程
def course(request):
    pass


# 名师风采及详细页
def teacher(request):
    pass


# 推荐阅读
def suggerst_read(request):
    pass


# 底部
def bottom(request):
    pass
