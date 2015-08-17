# -*- coding: utf-8 -*-
from django.test import TestCase
from django.views.generic import View
# Create your tests here.

class Test(object):
	def hello(self):
		pass
t=Test()
getattr(t,"hello1")