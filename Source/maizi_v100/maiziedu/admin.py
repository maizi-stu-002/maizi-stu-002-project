#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'qq_number', 'mobile', 'city')


admin.site.register(UserProfile, UserProfileAdmin)  # 用户
admin.site.register(CountryDict)  # 国家
admin.site.register(ProvinceDict)  # 省份
admin.site.register(CityDict)  # 城市
admin.site.register(Certificate)  # 证书
admin.site.register(BadgeDict)  # 徽章
admin.site.register(Student)  # 学生
admin.site.register(Teacher)  # 教师
admin.site.register(MyCourse)  # 我的课程
admin.site.register(BlogComment)  # 博客评论
admin.site.register(BlogCategoryDict)  # 博客分类
admin.site.register(Blog)  # 博客
admin.site.register(Keywords)  # 博客关键字
admin.site.register(PlanningItem)  # 计划事项
admin.site.register(Planning)  # 计划
admin.site.register(Class)  # 班级
admin.site.register(UserPurchase)  # 用户购买信息
admin.site.register(CareerCourse)  # 职业课程
admin.site.register(Stage)  # 课程阶段
admin.site.register(Course)  # 课程
admin.site.register(Lesson)  # 课时
admin.site.register(LessonResource)  # 课程资源
admin.site.register(Discuss)  # 课程讨论
admin.site.register(UserLearnLesson)  # 用户学习课时
admin.site.register(UserFavoriteCourse)  # 用户收藏
admin.site.register(Ad)  # 广告
