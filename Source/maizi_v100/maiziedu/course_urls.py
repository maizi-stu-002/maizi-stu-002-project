from django.conf.urls import include, url
from django.contrib import admin
from course_views import *
urlpatterns = [
	url(r'^course$', course ,name="course"),
]
