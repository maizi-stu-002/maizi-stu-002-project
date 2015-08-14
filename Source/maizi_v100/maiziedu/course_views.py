# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
# Create your views here.
def course_globals(request):
	deadlink = "javascript:;"
	return locals()

# 分页
def getPage(request, course_list):
	paginator = Paginator(course_list, 9)
	try:
	    page = int(request.GET.get('page', 1))
	    course_list = paginator.page(page)
	except (EmptyPage, InvalidPage, PageNotAnInteger):
	    course_list = paginator.page(1)

	return course_list

# 课程列表
def course(request):
	return render(request, "course.html", locals())