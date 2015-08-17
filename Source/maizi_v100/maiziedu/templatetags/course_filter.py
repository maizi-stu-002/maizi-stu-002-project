# -*- coding: utf-8 -*-
from django.template import Library
register = Library()

@register.filter
def getHourMinute(minute):
	t_hours = minute/60
	t_min = minute - t_hours*60
	return "%s小时%s分钟" % (t_hours, t_min)