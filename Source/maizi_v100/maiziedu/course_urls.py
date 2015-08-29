from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from course_views import *


urlpatterns = [
	# url(r'course/(?P<pageId>\d{1,2})?/?$'
	url(r'^course/', include([
		url(r'^$', CourseListView.as_view(),name="course_list"),
		url(r'^add/comment/$', AddCommentView.as_view(), name="addComment"),
		])
	),
	url(r'^lesson/', include([
		url(r'^(?P<lid>\d+)/', include([
			url(r'^$', LessonRedirectView.as_view(), name="lesson"),
			url(r'^comment/$', get_comments_view, name="lessonComment"),
			])
		),
		url(r'^student/job/upload/$', UploadView.as_view(), name="upload"),
		])
	),
	url(r'^course/',
		include([
			url(r'^(?P<name>[\w-]+)/',
				include([
					url(r'^$', CourseStageView.as_view(), name="course_stage"),
					url(r'^(?P<cid>\d+)-(?P<lid>\d+)/$', LessonPlayView.as_view(), name="course_play"),
				])
				),
			url(r'^(?P<cid>\d+)/',
				include([
					url(r'^recent/play/$', RecentPlayView.as_view(), name="recent_play"),
					url(r'^favorite/update/$', FavoriteUpdateView.as_view(), name="favorite_update"),
				])
				),
		]),
	),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
