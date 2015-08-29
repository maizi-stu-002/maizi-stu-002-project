# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import (CareerCourse, Course, UserLearnLesson, Lesson,
 UserFavoriteCourse, LessonResource, Teacher, Discuss)
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
import os
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
    template_name = "course_stage.html"

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

    @method_decorator(login_required)
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

class LessonRedirectView(View):

    def get(self, request, lid):
        lesson = get_object_or_404(Lesson,pk=lid)
        return HttpResponseRedirect(reverse(
                'course_play',
                kwargs={
                    'name':lesson.course.stage.career_course.symbol,
                    'cid':lesson.course.id,
                    'lid':lid,
                }
            ))

# 检查子级评论
def check_comment(c, d={}):
    pid = c.parent_id
    try:
        assert pid
    except AssertionError:
        # 父级评论
        d.setdefault(c.id, [])
    else:
        # 子级评论
        d.setdefault(pid, [])
        _ = d.get(pid)
        _.append(c)
    finally:
        return d
# 获取评论
def get_comments(comment_of_lesson):
    try:
        assert comment_of_lesson
    except AssertionError:
        comments = []
    else:
        mapping = map(check_comment, comment_of_lesson)[0]
        # 父级评论
        p_comment = comment_of_lesson.filter(pk__in = mapping.keys()).order_by("-date_publish")
        def x(y):
            setattr(y, 'subcomment', mapping.get(y.id))
            return y
        comments = map(x, p_comment)
        # 清除映射
        mapping.clear()
    finally:
        return comments
# 课程播放

class LessonPlayView(DetailView):
    template_name = "course_play.html"
    pk_url_kwarg = "lid"
    
    def get_queryset(self):
        self.course = get_object_or_404(Course, pk=self.kwargs.get('cid'))
        self.lessonToPlay = get_object_or_404(Lesson, pk=self.kwargs.get('lid'))
        comment_of_lesson = Discuss.objects.filter(lesson=self.lessonToPlay).order_by("pk")
        self.studentCount = UserLearnLesson.objects.filter(lesson=self.lessonToPlay).count() - 1
        self.lessonResource = LessonResource.objects.filter(lesson=self.lessonToPlay)
        self.is_user = self.request.user.is_authenticated()
        #get all comments
        self.comments = get_comments(comment_of_lesson)

        if self.is_user:
            self.housed = UserFavoriteCourse.objects.filter(
            course=self.course,
            student__user=self.request.user)
            self.is_teacher = Teacher.objects.filter(user=self.request.user)
        else:
            self.housed = False

        return self.course.lesson_set.all()
    
    def get_context_data(self, **kwargs):
        context = super(LessonPlayView, self).get_context_data(**kwargs)
        context['course'] = self.course
        context['lesson_to_play'] = self.lessonToPlay
        context['studentCount'] = self.studentCount
        context['housed'] = self.housed
        context['user'] = self.request.user
        context['is_user'] = self.is_user
        context['is_teacher'] = self.is_user and self.is_teacher
        context['comments'] = self.comments
        context['lessonResource'] = self.lessonResource
        context['uploadFileForm'] = UploadFileForm()
        context['upload_file_exists'] = True if os.path.isfile(
            os.path.join(settings.MEDIA_ROOT, "job/uid%s_lid%s.zip")%(self.request.user.id, self.lessonToPlay.id)) else False
        return context

    def get_object(self):
        # Call the superclass
        lesson = super(LessonPlayView, self).get_object()
        # Record the recent-played lesson
        if self.is_user:
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

# upload
class UploadView(View):

    @method_decorator(csrf_protect)
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            self.handle_uploaded_file(request)
            return JsonResponse({'status':200})
        else:
            return JsonResponse(form.errors, status=404)

    def handle_uploaded_file(self, req):
        f = req.FILES['FileData']
        lid = req.POST['lesson_id']
        uid = req.user.id
        t_dir = os.path.join(settings.MEDIA_ROOT,"job")
        if not os.path.exists(t_dir):
            os.makedirs(t_dir)
        os.chdir(t_dir)
        with open('uid%s_lid%s.zip'%(uid, lid), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

# 增加课时评论
class AddCommentView(View):

    @method_decorator(login_required)
    def post(self, request):
        p = request.POST
        d = {}
        d['lesson_id'] = p.get("lesson_id")
        d['content'] = p.get("comment","")
        d['parent_id'] = p.get("parent_id")
        d['user'] = request.user
        try:
            Discuss.objects.create(**d)
        except Exception:
            return JsonResponse({'status':400})
        else:
            return JsonResponse({'status':200})
# 获取评论
def get_comments_view(request, lid):
    lessonToPlay = get_object_or_404(Lesson, pk=lid)
    comment_of_lesson = Discuss.objects.filter(lesson=lessonToPlay).order_by("pk")
    comments = get_comments(comment_of_lesson)
    return render(request, "course_comment.html",{'comments':comments})
