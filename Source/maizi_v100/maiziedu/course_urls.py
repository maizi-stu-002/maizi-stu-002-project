from django.conf.urls import include, url
from django.contrib import admin
import course_views
urlpatterns = [
	# url(r'course/(?P<pageId>\d{1,2})?/?$'
	url(r'^course$',course_views.course,name="course"),
	url(r'^course/',include([
		url(r'^andriod/$',course_views.details,name="andriod"),

	])),
]
