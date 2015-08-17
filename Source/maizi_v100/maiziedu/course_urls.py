from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from course_views import *
urlpatterns = [
	# url(r'course/(?P<pageId>\d{1,2})?/?$'
	url(r'^course/$',course,name="course"),
	url(r'^course/',
		include([
			url(r'^(?P<name>[\w-]+)/$',
				CourseView.as_view()),

		])
	),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
