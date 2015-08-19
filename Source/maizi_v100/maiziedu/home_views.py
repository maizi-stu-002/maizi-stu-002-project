#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.conf import settings
from models import *

logger = logging.getLogger('maiziedu.home_views')


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
        home_page = settings.HOME_PAGE  # 网站首页
        about_us = settings.ABOUT_US  # 关于我们
        contact_us = settings.CONTACT_US  # 联系我们
        join_us = settings.JOIN_US  # 加入我们
        # 关注我们
        weibo_sina = settings.WEIBO_SINA  # 新浪微博
        weibo_tencent = settings.WEIBO_TENCENT  # 腾讯微博
        weixin = settings.WEIXIN  # 官方微信
        # 课程
        new_add = Course.objects.order_by('-date_publish')  # 最新课程
        # 最新课程分页
        new_add = get_page(request, new_add)

        most_play = Course.objects.order_by('-play_count')  # 最多播放
        # 最多播放分页
        most_play = get_page(request, most_play)

        hot_favorite = Course.objects.order_by('-favorite_count')  # 最具人气
        # 最具人气分页
        hot_favorite = get_page(request, hot_favorite)
        return render(request, 'home/index.html', locals())
    except Exception as e:
        logger.error(e)


# 分页代码
def get_page(request, course_list):
    paginator = Paginator(course_list, 8)  # 一页最多显示8门课程
    try:
        page = int(request.GET.get('page', 1))
        course_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        course_list = paginator.page(1)  # 出现异常就返回第一页
    return course_list
