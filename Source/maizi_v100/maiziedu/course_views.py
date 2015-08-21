# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import CareerCourse, Course, UserLearnLesson, Lesson
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.timezone import now
from django.core.urlresolvers import reverse
# Create your views here.


def course_globals(request):
    deadlink = "javascript:;"
    return locals()


# 课程列表
class CourseListView(ListView):
    model = CareerCourse

    def get(self, request):
        try:
            assert request.is_ajax()
        except AssertionError:
            template_name = "course.html"
        else:
            template_name = "course_ajax.html"
        # 使用通用视图
        # paginate_queryset(queryset, page_size)
        # Returns a 4-tuple containing (paginator, page, object_list,
        # is_paginated).
        page = self.paginate_queryset(self.get_queryset(), 6)[1]
        return render(request, template_name, locals())


# 课程阶段
class CourseStageView(DetailView):
    model = CareerCourse

    def get(self, request, name):
        career = get_object_or_404(self.get_queryset(), symbol=name)
        return render(request, "details.html", locals())


# 最近播放
class RecentPlayView(DetailView):

    def get(self, request, cid):
        course = get_object_or_404(Course, pk=cid)
        name = course.stage.career_course.symbol
        lesson = self.get_recent_played_lesson(request, cid)
        return HttpResponseRedirect(
            reverse("course_play", kwargs={'name': name, 'cid': cid, 'lid': lesson.id}))

    def get_recent_played_lesson(self, request, cid):
        try:
            ulesson = UserLearnLesson.objects.filter(
                lesson__course=cid, student__user=request.user)
            assert ulesson
        except AssertionError:
            lesson = get_object_or_404(Course, pk=cid).lesson_set.all()[0]
        else:         
            lesson = ulesson.order_by("-date_learning")[0].lesson
        finally:
            return lesson


# 课程播放
class CoursePlayView(ListView):
    model = Course

    def get(self, request, name, cid, lid):
        course = get_object_or_404(self.get_queryset(), pk=cid)
        lesson_to_play = get_object_or_404(Lesson, pk=lid)
        try:
            assert request.user.is_authenticated()
        except AssertionError:
            pass
        else:
            self.update_recent_played_lesson(request, lid)
        finally:
            studentCount = UserLearnLesson.objects.filter(lesson=lesson_to_play).count()-1
            return render(request, "course_play.html", locals())

    def update_recent_played_lesson(self, request, lid):
        # 判断该课时是否由该用户观看过
        try:
            ulesson = UserLearnLesson.objects.filter(
                lesson=lid, student__user=request.user)
            assert ulesson
        except AssertionError:
            # 新建观看的记录
            UserLearnLesson.objects.create(
                student=request.user.student,
                lesson=get_object_or_404(Lesson,pk=lid)
            )
        else:
            # 更新最后观看的时间
            ulesson.update(date_learning=now())

