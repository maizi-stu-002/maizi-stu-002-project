#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.conf import settings
from models import *

logger = logging.getLogger('maiziedu.home_views')


# 首页全局信息配置
def home_globals(request):
    # 媒体信息配置
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
    # 最新课程
    new_add = Course.objects.order_by('-date_publish')
    new_add = get_page(request, new_add)
    # 最多播放
    most_play = Course.objects.order_by('-play_count')
    most_play = get_page(request, most_play)
    # 最具人气
    hot_favorite = Course.objects.order_by('-favorite_count')
    hot_favorite = get_page(request, hot_favorite)
    # 推荐阅读
    official_activity = RecommendRead.objects.filter(category='1').order_by('-date_publish')[:5]  # 官方活动
    technology_exchange = RecommendRead.objects.filter(category='2').order_by('-date_publish')[:5]  # 技术交流
    developer_information = RecommendRead.objects.filter(category='3').order_by('-date_publish')[:5]  # 开发者资讯
    # 关键字
    keyword_list = Keywords.objects.all()[:6]

    return locals()


# 首页
def index(request):
    try:
        return render(request, 'home/index.html', locals())
    except Exception as e:
        logger.error(e)


# 教师详情页面
def has_course(request, teacher_id):
    try:
        # 按照id匹配教师
        teacher = Teacher.objects.get(pk=teacher_id)
        # 教师课程列表
        course_list = teacher.course_set.all()
        return render(request, 'has_course.html', locals())
    except Exception as e:
        logger.error(e)


# 搜索结果
def search_results(request):
    try:
        keyword = request.GET.get('keyword', '')
        if keyword:
            qset = (
                Q(name__icontains=keyword) | Q(description__icontains=keyword)
            )
            # 职业课程
            career_course_list = []
            career_courses = CareerCourse.objects.filter(qset).distinct()
            for career_course in career_courses:
                career_course_dict = {
                    'name': career_course.name,
                    'course_color': career_course.course_color,
                    'id': career_course.id,
                    # 'img_url': career_course.img_url,
                }
                career_course_list.append(career_course_dict)

            # 课程
            course_list = []
            courses = Course.objects.filter(qset).distinct()
            for course in courses:
                course_dict = {
                    'name': course.name,
                    # 'img_url': course.img_url,
                    'id': course.id,
                    'stage_id': course.stage.id,
                    'course_color': course.course_color,
                }
                course_list.append(course_dict)
            results = {'career_courses': career_course_list, 'courses': course_list}
        else:
            results = []
        print results
        data = json.dumps(results)
        print data
        content_type = 'application/json'
        return HttpResponse(data, content_type)
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
