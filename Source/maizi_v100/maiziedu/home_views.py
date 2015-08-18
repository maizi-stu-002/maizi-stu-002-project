#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.shortcuts import render
from models import *
from django.conf import settings

logger = logging.getLogger('maiziedu.home_views')


# 全局信息
def global_setting(request):
    pass


# 首页
def index(request):
    try:
        # 媒体信息
        media_url = settings.MEDIA_URL
        # 广告
        ad_list = Ad.objects.all()[:6]
        # 教师
        teacher_list = Teacher.objects.all()
        # 战略合作
        strategic_list = Strategic.objects.all()
        # 友情链接
        link_list = Links.objects.all()
        # 网站导航
        home_page = settings.HOME_PAGE
        about_us = settings.ABOUT_US
        contact_us = settings.CONTACT_US
        join_us = settings.JOIN_US
        # 关注我们
        weibo_sina = settings.WEIBO_SINA
        weibo_tencent = settings.WEIBO_TENCENT
        weixin = settings.WEIXIN
        return render(request, 'home/index.html', locals())
    except Exception as e:
        logger.error(e)


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
