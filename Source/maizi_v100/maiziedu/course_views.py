# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import Http404,HttpResponse
# Create your views here.


def course_globals(request):
	deadlink = "javascript:;"
	return locals()

def common_views(request, name,*arg,**kwags):
	print name
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
def course(request,*arg, **kwags):
	colors = (
		"#A9BE32",
		"#E68E38",
		"#429FDA",
		"#D3A21F",
		"#EE5C5C",
		"#35AC56",
	)
	data_list = [
		{
			"name":"Android应用开发工程师",
			"people":123123,
			"imgurl":"images/course/android.png",
			"bgc":colors[0]
		},
		{
			"name":"Android应用开发工程师",
			"people":123123,
			"imgurl":"images/course/android.png",
			"bgc":colors[1]
		},
		{
			"name":"Android应用开发工程师",
			"people":123123,
			"imgurl":"images/course/android.png",
			"bgc":colors[2]
		},
		{
			"name":"Android应用开发工程师",
			"people":123123,
			"imgurl":"images/course/android.png",
			"bgc":colors[3]
		},
		{
			"name":"Android应用开发工程师",
			"people":123123,
			"imgurl":"images/course/android.png",
			"bgc":colors[4]
		},
		{
			"name":"Android应用开发工程师",
			"people":123123,
			"imgurl":"images/course/android.png",
			"bgc":colors[5]
		},
	]*5
	page = getPage(request, getPaginator(data_list, 9))
	return render(request, "course.html", locals())

def details(request):
	return render(request, "details.html", locals())
