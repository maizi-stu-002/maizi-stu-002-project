#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<center><h1><cneter>欢迎来到麦子官网1.0项目，下面，让我们开始愉快地干活吧^_^</h1></center>')
