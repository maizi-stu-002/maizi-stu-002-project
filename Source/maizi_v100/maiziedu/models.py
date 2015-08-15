# -*- coding: utf-8 -*-
from django.db import models
import random

# Create your models here.

class CourseManager(models.Manager):

	def exclude_duplicated(seq):
		try:
			length = len(seq)
		except TypeError:
			return False
		else:
			# 对应seq索引值的区间
			m,n = 0,length-1
		try:
			ex = int(length)
		except ValueError:
			ex = -1
		finally:
			if ex>0:
				ex = -ex
			elif ex is 0:
				ex = -1
		def _ex(last_randints=[]):
			while 1:
				cur_randint = random.randint(m,n)
				if duplicate:
					break
				elif cur_randint not in last_randints[ex:]:
					last_randints.append(cur_randint)
					break
			return cur_randint
		return _ex


class Course(models.Model):
	objects = CourseManager()
