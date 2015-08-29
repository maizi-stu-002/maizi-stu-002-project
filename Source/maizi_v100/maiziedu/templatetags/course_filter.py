# -*- coding: utf-8 -*-
from django.template import Library
from django.utils.timesince import timesince
import re

register = Library()

SUBSTITUTE = {
    re.compile('^minute(s)?(,)?$'): u'分钟',
    re.compile('^hour(s)?(,)?$'): u'小时',
    re.compile('^day(s)?(,)?$'): u'天',
    re.compile('^week(s)?(,)?$'): u'周',
    re.compile('^month(s)?(,)?$'): u'月',
    re.compile('^year(s)?(,)?$'): u'年',
}


def substitute(n):
    for k, v in SUBSTITUTE.items():
        if k.match(n):
            return v
    else:
        return n


@register.filter(expects_localtime=True)
def postsince(d):
    if timesince(d).startswith("0"):
        result = u'刚刚'
    else:
        result = " ".join(map(substitute, timesince(d).split())) + u'前'
    return result

@register.filter
def getHourMinute(minute):
	t_hours = minute/60
	t_min = minute - t_hours*60
	return "%s小时%s分钟" % (t_hours, t_min)