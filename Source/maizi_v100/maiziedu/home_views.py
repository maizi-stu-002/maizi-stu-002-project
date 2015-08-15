#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render


# 首页
def index(request):
    return render(request, 'base.html', locals())
