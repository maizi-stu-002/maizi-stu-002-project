# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import CareerCourse, Course, UserLearnLesson, Lesson, UserFavoriteCourse
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


def course_globals(request):
    deadlink = "javascript:;"
    return locals()


# 课程列表
class CourseListView(ListView):
    model = CareerCourse
    template_name = "course.html"
    # context_object_name = "page"

    def get_context_data(self, **kwargs):
        if self.request.is_ajax():
            self.template_name = "course_ajax.html"
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['page'] = self.paginate_queryset(self.get_queryset(), 6)[1]
        return context


# 课程阶段
class CourseStageView(ListView):
    template_name = "details.html"

    def get_queryset(self):
        self.career = get_object_or_404(
            CareerCourse, symbol=self.kwargs['name'])

    def get_context_data(self, **kwargs):
        context = super(CourseStageView, self).get_context_data(**kwargs)
        context['career'] = self.career
        context['login'] = self.request.user.is_authenticated()
        return context

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
class LessonPlayView(DetailView):
    template_name = "course_play.html"
    pk_url_kwarg = "lid"

    def get_queryset(self):
        self.course = get_object_or_404(Course, pk=self.kwargs.get('cid'))
        self.lessonToPlay = get_object_or_404(Lesson, pk=self.kwargs.get('lid'))
        self.studentCount = UserLearnLesson.objects.filter(lesson=self.lessonToPlay).count() - 1
        if self.request.user.is_authenticated():
            self.housed = UserFavoriteCourse.objects.filter(
            course=self.course,
            student__user=self.request.user)
        else:
            self.housed = False

        return self.course.lesson_set.all()

    def get_context_data(self, **kwargs):
        context = super(LessonPlayView, self).get_context_data(**kwargs)
        context['course'] = self.course
        context['lesson_to_play'] = self.lessonToPlay
        context['studentCount'] = self.studentCount
        context['housed'] = self.housed
        return context

    def get_object(self):
        # Call the superclass
        lesson = super(LessonPlayView, self).get_object()
        # Record the recent-played lesson
        if self.request.user.is_authenticated():
            self.update_recent_played_lesson()  
        # Return the object
        return lesson

    def update_recent_played_lesson(self):
        # 判断该课时是否由该用户观看过
        lid = self.kwargs.get("lid")
        user = self.request.user
        try:
            ulesson = UserLearnLesson.objects.filter(
                lesson=lid, student__user=user)
            assert ulesson
        except AssertionError:
            # 新建观看的记录
            UserLearnLesson.objects.create(
                student=user.student,
                lesson=get_object_or_404(Lesson, pk=lid)
            )
        else:
            # 更新最后观看的时间
            ulesson.update(date_learning=now())


class FavoriteUpdateView(View):

    def get(self,request,cid):
        if not request.user.is_authenticated():
            return HttpResponse("notuser")
        favorite_course = UserFavoriteCourse.objects.filter(
            course=cid,
            student__user=request.user)
        try:
            assert favorite_course
        except AssertionError:
            UserFavoriteCourse.objects.create(
                student=request.user.student,
                course=get_object_or_404(Course, pk=cid),
            )
            message = "houseok"
        else:
            favorite_course.delete()
            message = "housecancel"
        finally:
            return HttpResponse(message)



