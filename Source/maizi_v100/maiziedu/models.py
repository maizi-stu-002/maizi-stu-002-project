#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户信息模型
class UserProfile(AbstractUser):
    avatar_url = models.ImageField(u'头像地址', upload_to='avatar/%Y/%m', default='avatar/default.png',
                                   max_length=200, blank=True)
    avatar_thumbnail_url = models.ImageField(u'头像缩略图地址', upload_to='avatar_thumbnail/%Y/%m',
                                             default='avatar_thumbnail/default.png', max_length=200, blank=True)
    nick_name = models.CharField(u'昵称', max_length=50, blank=True)
    teacher_description = models.CharField(u'任课教师描述', max_length=200, blank=True)
    qq_number = models.CharField(u'qq号', max_length=20, blank=True)
    mobile = models.CharField(u'手机号', max_length=11, blank=True, unique=True)
    company_name = models.CharField(u'公司名称', max_length=150, blank=True)
    position = models.CharField(u'地址', max_length=150, blank=True)
    city = models.ForeignKey('CityDict', null=True, blank=True)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


# 国家
class CountryDict(models.Model):
    name = models.CharField(u'国家', max_length=50, blank=True)

    class Meta:
        verbose_name = u'国家'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 省份
class ProvinceDict(models.Model):
    name = models.CharField(u'省份', max_length=50, blank=True)
    country = models.ForeignKey('CountryDict')

    class Meta:
        verbose_name = u'省份'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 城市
class CityDict(models.Model):
    name = models.CharField(u'城市', max_length=50, blank=True)
    province = models.ForeignKey('ProvinceDict')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 证书
class Certificate(models.Model):
    name = models.CharField(u'证书名称', max_length=50)
    image_url = models.ImageField(u'证书图片地址', upload_to='certificate/%Y/%m', max_length=200, blank=True)

    class Meta:
        verbose_name = u'证书'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 徽章
class BadgeDict(models.Model):
    name = models.CharField(u'徽章名称', max_length=50)
    badge_url = models.ImageField(u'徽章地址', upload_to='badge/%Y/%m', max_length=200, blank=True)

    class Meta:
        verbose_name = u'徽章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 学生
class Student(models.Model):
    user = models.OneToOneField('UserProfile', verbose_name=u'用户信息')
    certificate = models.ForeignKey('Certificate', verbose_name=u'证书')
    badge = models.ForeignKey('BadgeDict', verbose_name=u'徽章')
    student_class = models.ForeignKey('Class', verbose_name=u'学生班级')

    class Meta:
        verbose_name = u'学生'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username


# 教师
class Teacher(models.Model):
    user = models.OneToOneField('UserProfile', verbose_name=u'用户')
    position = models.CharField(max_length=50, verbose_name=u'职位')
    description = models.CharField(max_length=200, verbose_name=u'描述')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username


# 我的课程
class MyCourse(models.Model):
    course_type = (
        ('1', 'course'),  # 普通课程
        ('2', 'career_course'),  # 职业课程
    )
    course_type = models.CharField(u'课程类型', choices=course_type, max_length=1)
    course_id = models.IntegerField(u'课程id')
    date_learning = models.DateTimeField(u'学习时间')

    class Meta:
        verbose_name = u'我的课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s, %s, %s' % (self.course_type, self.course_id, self.date_learning)


# 博客评论
class BlogComment(models.Model):
    content = models.TextField(u'评论内容')
    is_subject = models.BooleanField(u'是否是主评论')
    date_publish = models.DateTimeField(u'发布日期', auto_now_add=True)

    class Meta:
        verbose_name = u'博客评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return '%s, %s' % (self.content, self.date_publish)


# 博客分类
class BlogCategoryDict(models.Model):
    name = models.CharField(u'分类名称', max_length=200)

    class Meta:
        verbose_name = u'博客分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 博客
class Blog(models.Model):
    title = models.CharField(u'标题', max_length=200)
    date_publish = models.DateTimeField(u'发布日期', auto_now_add=True)
    is_active = models.BooleanField(u'状态', default=True)
    content = models.TextField(u'内容', blank=True)
    comment = models.ManyToManyField(BlogComment, blank=True, verbose_name=u'评论')
    category = models.ManyToManyField(BlogCategoryDict, blank=True, verbose_name=u'分类')

    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return '%s, %s' % (self.title, self.date_publish)


# 博客关键字
class Keywords(models.Model):
    name = models.CharField(u'关键字', max_length=50, blank=True)
    blog = models.ManyToManyField(Blog, verbose_name=u'博客', blank=True)

    class Meta:
        verbose_name = u'博客关键字'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 计划事项
class PlanningItem(models.Model):
    start_date = models.DateTimeField(u'开始时间', auto_now_add=True, null=True, blank=True)
    end_date = models.DateTimeField(u'结束时间', null=True, blank=True)

    class Meta:
        verbose_name = u'计划事项'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s, %s' % (self.start_date, self.end_date)


# 计划
class Planning(models.Model):
    date_publish = models.DateTimeField(u'发布时间', auto_now_add=True)
    is_active = models.BooleanField(u'状态', default=True)
    version = models.IntegerField(u'版本')
    planning_item = models.ManyToManyField(PlanningItem, verbose_name=u'计划事件')

    class Meta:
        verbose_name = u'计划'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return '%s, %s' % (self.version, self.date_publish)


# 用户购买信息
class UserPurchase(models.Model):
    pay_type = (  # 购买类型
        ('1', 'VIP'),  # vip
        ('2', 'CareerCourse'),  # 职业课程
    )
    pay_stage = (  # 购买阶段
        ('0', 'all'),  # 所有阶段
        ('1', u'阶段一'),  # 阶段一
        ('2', u'阶段二'),  # 阶段二
    )
    pay_way = (  # 支付方式
        ('1', 'alipay'),  # 阿里支付宝
        ('2', 'kuaiqian'),  # 快钱
    )
    pay_status = (  # 支付状态
        ('1', 'success'),  # 成功
        ('2', 'failed'),  # 失败
    )
    pay_price = models.DecimalField(u'购买价格', max_digits=5, decimal_places=2)
    ording_coding = models.CharField(u'预定语言', max_length=200)
    trad_coding = models.CharField(u'交易语言', max_length=200, blank=True)
    pay_type = models.CharField(u'购买类型', choices=pay_type, max_length=1)
    pay_stage = models.CharField(u'购买阶段', choices=pay_stage, max_length=1)
    date_pay = models.DateTimeField(u'支付时间', auto_now_add=True)
    date_limit = models.DateTimeField(u'限制时间', null=True, blank=True)
    pay_way = models.CharField(u'支付方式', choices=pay_way, blank=True, max_length=1)
    pay_status = models.CharField(u'支付状态', choices=pay_status, blank=True, max_length=1)

    class Meta:
        verbose_name = u'用户购买信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s, %s, %s,%s' % (self.ording_coding, self.date_pay, self.date_limit, self.pay_status)


# 职业课程
class CareerCourse(models.Model):
    name = models.CharField(u'名称', max_length=50, blank=True)
    description = models.TextField(u'课程描述', blank=True)
    total_price = models.DecimalField(u'总共价格', max_digits=6, decimal_places=2)
    imgurl = models.CharField(u'图片路径',max_length=50,blank=False,null=True)
    symbol = models.CharField(u'代号',max_length=10,blank=False,null=True)
    purchase = models.ForeignKey(UserPurchase, verbose_name=u'用户购买', null=True, blank=True)
    planning = models.ForeignKey(Planning, verbose_name=u'课程计划', null=True, blank=True)
    def getCourses(self):
        # CareerCourse下所有course
        return (course for stage in self.stage_set.all() for course in stage.course_set.all())

    def getLessons(self):
        # CareerCourse下所有Lesssons
        return (lesson for course in self.getCourses() for lesson in course.lesson_set.all())

    def getUserCount(self):
        # 所有学习该课程的学生人数
        return UserLearnLesson.objects.filter(lesson__in=self.getLessons()).values('student').distinct().count()

    def getTimeToSpend(self):
        # 职业课程下所有视频累计时间
        return  sum(map(lambda x:x.video_length,self.getLessons()))

        

    class Meta:
        verbose_name = u'职业课程'
        verbose_name_plural = verbose_name
        ordering = ("name","id")

    def __unicode__(self):
        return '%s, %s' % (self.name, self.total_price)

# 班级
class Class(models.Model):
    code = models.CharField(u'何种语言', max_length=10)
    date_publish = models.DateTimeField(u'发布事件', auto_now_add=True)
    student_limit = models.IntegerField(u'学生人数限制', default=20, null=True, blank=True)
    current_student_count = models.IntegerField(u'现在学生人数', null=True, blank=True)
    is_active = models.BooleanField(u'状态', default=True)
    career_course = models.ForeignKey(CareerCourse, verbose_name=u'职业课程',null=True,blank=True)
    class Meta:
        verbose_name = u'班级'
        verbose_name_plural = verbose_name
        ordering = ['code', '-date_publish', 'is_active']

    def __unicode__(self):
        return self.code

# 课程阶段
class Stage(models.Model):
    name = models.CharField(u'阶段名称', max_length=50)
    description = models.CharField(u'描述', max_length=200)
    index = models.IntegerField(u'序号', null=True, blank=True)
    career_course = models.ForeignKey(CareerCourse, verbose_name=u'所属职业课程')

    class Meta:
        verbose_name = u'课程阶段'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 课程（职业课程子课程）
class Course(models.Model):
    name = models.CharField(u'名称', max_length=50)
    description = models.CharField(u'描述', max_length=200)
    is_active = models.BooleanField(u'状态', default=True)
    date_publish = models.DateTimeField(u'发布日期', auto_now_add=True)
    need_days = models.IntegerField(u'完成需要天数', null=True, blank=True)
    index = models.IntegerField(u'序号', null=True, blank=True)
    stage = models.ForeignKey(Stage, verbose_name=u'所属阶段')
    planning_item = models.ForeignKey(PlanningItem, verbose_name=u'课程计划')
    teacher = models.ForeignKey(Teacher, verbose_name=u'任课教师')
    avatarUrl = models.ImageField(upload_to="course",default="course/default.jpg",verbose_name=u"课程缩略图",null=True,blank=True)

    def getTimeToSpend(self):
        return sum([lesson.video_length for lesson in self.lesson_set.all()])

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish', 'is_active']

    def __unicode__(self):
        return self.name


# 课时（课程具体的每节课）
class Lesson(models.Model):
    name = models.CharField(u'名称', max_length=50)
    video_url = models.CharField(u'视频地址', max_length=200)
    video_length = models.IntegerField(u'视频长度')
    pay_count = models.IntegerField(u'付费计数', null=True, blank=True)
    index = models.IntegerField(u'序号', null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name=u'所属课程')

    class Meta:
        verbose_name = u'课时'
        verbose_name_plural = verbose_name
        ordering = ('index','name')
    def __unicode__(self):
        return self.name


# 课程资源
class LessonResource(models.Model):
    name = models.CharField(u'名称', max_length=50, blank=True)
    resource = models.FileField(upload_to="lesson",verbose_name=u"课件",null=True,blank=True)
    # download_url = models.CharField(u'下载地址', max_length=200, blank=True)
    download_count = models.IntegerField(u'下载计数', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, verbose_name=u'所属课时')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 课时讨论
class Discuss(models.Model):
    content = models.TextField(u'讨论内容')
    parent_id = models.IntegerField(u'父编号', null=True, blank=True)
    date_publish = models.DateTimeField(u'发布日期', auto_now_add=True)
    lesson = models.ForeignKey(Lesson, verbose_name=u'所属课时')
    user = models.ForeignKey(UserProfile, verbose_name=u'用户',null=True)

    class Meta:
        verbose_name = u'课时讨论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return "-".join([
            str(self.pk),
            self.lesson.name,
         self.user.username,
         str(self.parent_id),
                    ]) 


# 用户学习课时
class UserLearnLesson(models.Model):
    date_learning = models.DateTimeField(u'学习日期', auto_now_add=True)
    student = models.ForeignKey(Student, verbose_name=u'学生', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, verbose_name=u'课时', null=True, blank=True)

    class Meta:
        verbose_name = u'学习课时'
        verbose_name_plural = verbose_name
        unique_together = ('student', 'lesson')

    def __unicode__(self):
        return self.student.user.username + "-" + self.lesson.name


# 用户收藏的课程
class UserFavoriteCourse(models.Model):
    date_favorite = models.DateTimeField(u'喜欢时间', auto_now_add=True)
    course = models.ForeignKey(Course, verbose_name=u'收藏课程', null=True, blank=True)
    student = models.ForeignKey(Student, verbose_name=u'学生', null=True, blank=True)

    class Meta:
        verbose_name = u'收藏课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.student.user.username + "-" + self.course.name


# 广告
class Ad(models.Model):
    title = models.CharField(u'标题', max_length=50)
    description = models.CharField(u'描述', max_length=200, blank=True)
    img_utl = models.ImageField(u'图片链接', upload_to='ad/%Y/%m', max_length=200)
    callback_url = models.CharField(u'回调函数链接', max_length=200)

    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


# 设置
class Setting(models.Model):
    """
    学过的课程用时 = 课程用时 × 乘积参数 + 天数调整
    """
    score_pass_line = models.IntegerField(u'课程通过分数线',default=60)
    course_days_rule = models.IntegerField(u'课程用时', null=True, blank=True)
    know_course_percent = models.FloatField(u'乘积参数', null=True, blank=True)
    know_course_value = models.IntegerField(u'天数调整', null=True, blank=True)

    class Meta:
        verbose_name = u'设置'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'学过的课程用时： %s' % (self.course_days_rule * self.course_days_rule + self.know_course_value)


# # 日志
# class Log(models.Model):
#     action_type = (
#         ('1', u'系统消息'),
#         ('2', u'课程消息回复'),
#         ('3', u'论坛消息回复'),
#     )
#     userA = models.IntegerField(u'用户A')
#     userB = models.IntegerField(u'用户B', null=True, blank=True)
#     action_type = models.CharField(u'类型', choices=action_type, max_length=1, blank=True)
#     action_id = models.IntegerField(u'编号', null=True, blank=True)
#     date_action = models.DateTimeField(u'日期', auto_now_add=True)
#
#     class Meta:
#         verbose_name = u'日志'
#         verbose_name_plural = verbose_name
#         ordering = ['-date_action']
#
#     def __unicode__(self):
#         return self.action_type
#
#
# # 我的消息
# class MyMessage(models.Model):
#     action_type = (
#         ('1', u'系统消息'),
#         ('2', u'课程消息回复'),
#         ('3', u'论坛消息回复'),
#     )
#     userA = models.IntegerField(u'用户A')
#     userB = models.IntegerField(u'用户B', null=True, blank=True)
#     action_type = models.CharField(u'类型', choices=action_type, max_length=1, blank=True)
#     action_id = models.IntegerField(u'编号', null=True, blank=True)
#     date_action = models.DateTimeField(u'日期', auto_now_add=True)
#     is_new = models.BooleanField(u'是否为最新', default=True)
#
#     class Meta:
#         verbose_name = u'我的消息'
#         verbose_name_plural = verbose_name
#         ordering = ['is_new']
#
#     def __unicode__(self):
#         return self.action_type

