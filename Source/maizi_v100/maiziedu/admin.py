#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'qq_number', 'mobile', 'city')
admin.site.register(UserProfile, UserProfileAdmin)  # 用户


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_class')
admin.site.register(Student, StudentAdmin)  # 学生


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'description')
admin.site.register(Teacher, TeacherAdmin)  # 教师


admin.site.register(CountryDict)  # 国家
admin.site.register(ProvinceDict)  # 省份
admin.site.register(CityDict)  # 城市
admin.site.register(Certificate)  # 证书
admin.site.register(BadgeDict)  # 徽章


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'date_learning', 'course_type')
admin.site.register(MyCourse, MyCourseAdmin)  # 我的课程


admin.site.register(BlogComment)  # 博客评论
admin.site.register(BlogCategoryDict)  # 博客分类


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'is_active', 'date_publish')
admin.site.register(Blog, BlogAdmin)  # 博客


admin.site.register(Keywords)  # 关键字
admin.site.register(PlanningItem)  # 计划事项
admin.site.register(Planning)  # 计划


class ClassAdmin(admin.ModelAdmin):
    list_display = ('code', 'current_student_count', 'student_limit', 'is_active', 'date_publish')
admin.site.register(Class, ClassAdmin)  # 班级


admin.site.register(UserPurchase)  # 用户购买信息


class CareerCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'total_price')
admin.site.register(CareerCourse, CareerCourseAdmin)  # 职业课程


admin.site.register(Stage)  # 课程阶段


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'teacher', 'need_days', 'date_publish')
admin.site.register(Course, CourseAdmin)  # 课程


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_length', 'course')
admin.site.register(Lesson, LessonAdmin)  # 课时


class LessonResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'download_url', 'download_count', 'lesson')
admin.site.register(LessonResource, LessonResourceAdmin)  # 课程资源


admin.site.register(Discuss)  # 课程讨论
admin.site.register(UserLearnLesson)  # 用户学习课时
admin.site.register(UserFavoriteCourse)  # 用户收藏的课程


class StrategicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_publish')
admin.site.register(Strategic, StrategicAdmin)  # 战略合作


class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_publish')
admin.site.register(Links, LinksAdmin)  # 友情链接


admin.site.register(Ad)  # 广告
admin.site.register(Setting)  # 设置
admin.site.register(Log)  # 消息日志
admin.site.register(MyMessage)  # 我的消息
admin.site.register(ExamineRecord)  # 测试记录
admin.site.register(MissionRecord)  # 任务记录
admin.site.register(HomeworkRecord)  # 课后作业记录
admin.site.register(CodeExciseRecord)  # 在线编程记录
admin.site.register(QuizRecord)  # 小测试记录
admin.site.register(Examine)  # 测试
admin.site.register(Mission)  # 任务
admin.site.register(CodeExcise)  # 在线编程
admin.site.register(Quiz)  # 小测试
admin.site.register(Paper)  # 试卷
admin.site.register(Homework)  # 课后作业
