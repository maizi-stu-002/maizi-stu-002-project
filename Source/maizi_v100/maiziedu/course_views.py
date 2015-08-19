# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import Http404,HttpResponse
from .models import CareerCourse,Student,Class
from django.views.generic import View
# Create your views here.


def course_globals(request):
	deadlink = "javascript:;"
	return locals()

def common_views(request, name,*arg,**kwags):
	return globals()[name](request, *arg, **kwags)

def test(request):
	return HttpResponse("test")

# 分页
def getPaginator(obj_list, perPageNum):
	paginator = Paginator(obj_list, perPageNum)
	return paginator

def getPage(request, paginator):
	try:
	    page = int(request.GET.get('page', 1))
	    course_list = paginator.page(page)
	except (EmptyPage, InvalidPage, PageNotAnInteger):
	    course_list = paginator.page(1)
	return course_list

# 课程列表
def course(request):
	course_list = CareerCourse.objects.all()
	page = getPage(request, getPaginator(course_list, 6))
	return render(request, "course.html", locals())


class CourseView(View):
	def get(self, request,name):
		try:
			course = CareerCourse.objects.get(symbol=name)
		except CareerCourse.DoesNotExist:
			raise Http404()
		else:
			return render(request, "details.html", locals())
