from django.conf.urls import include, url
from django.contrib import admin
from student_views import *

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^my_center/learn_plan/', learn_plan, name='learn_plan'),
    url(r'^my_center/my_favorites', my_favorites, name='my_favorites'),
    url(r'^my_center/my_courses', my_courses, name='my_courses'),
    url(r'^my_center/my_certificates', my_certificates, name='my_certificates'),
    url(r'^my_center/my_messages', my_messages, name='my_messages'),
    url(r'^my_center/my_information', my_information, name='my_information'),
    url(r'^my_center/modify_email', modify_email, name='modify_email'),

]