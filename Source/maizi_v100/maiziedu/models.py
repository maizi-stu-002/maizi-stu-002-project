#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


# 设置
class Setting(models.Model):
    """
    学过的课程用时 = 课程用时 × 乘积参数 + 天数调整
    """
    score_pass_line = models.IntegerField(u'课程通过分数线', null=False)
    course_days_rule = models.IntegerField(u'课程用时')
    know_course_percent = models.FloatField(u'乘积参数')
    know_course_value = models.IntegerField(u'天数调整')

    class Meta:
        verbose_name = u'设置'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '学过的课程用时： %s' % (self.course_days_rule * self.course_days_rule + self.know_course_value)


class Log(models.Model):
    action_type = (
        ('1', '系统消息'),
        ('2', '课程消息回复'),
        ('3', '论坛消息回复'),
    )
    userA = models.IntegerField(u'用户A', null=False)
    userB = models.IntegerField(u'用户B')
    action_type = models.CharField(u'类型', choice=action_type, max_length=1)
    action_id = models.IntegerField(u'编号')
    date_action = models.DateTimeField(u'日期', null=False)

    class Meta:
        verbose_name = '日志'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.action_type


# 我的消息
class MyMessage(models.Model):
    action_type = (
        ('1', '系统消息'),
        ('2', '课程消息回复'),
        ('3', '论坛消息回复'),
    )
    userA = models.IntegerField(u'用户A', null=False)
    userB = models.IntegerField(u'用户B')
    action_type = models.CharField(u'类型', choice=action_type, max_length=1)
    action_id = models.IntegerField(u'编号')
    date_action = models.DateTimeField(u'日期', null=False)
    is_new = models.BooleanField(u'是否为最新', default=True)

    class Meta:
        verbose_name = '我的消息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.action_type


# 广告
class Ad(models.Model):
    title = models.CharField(u'标题', max_length=50, null=False)
    description = models.CharField(u'描述', max_length=200)
    img_utl = models.CharField(u'图片链接', max_length=200, null=False)
    callback_url = models.CharField(u'回调函数链接', max_length=200, null=False)

    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


# 国家字典
class CountryDict(models.Model):
    name = models.CharField(u'国家', max_length=50)

    class Meta:
        verbose_name = u'国家'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 省份字典
class ProveceDict(models.Model):
    name = models.CharField(u'省份', max_length=50)
    country = models.ForeignKey(CountryDict)

    class Meta:
        verbose_name = u'省份'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 城市字典
class CityDict(models.Model):
    name = models.CharField(u'城市', max_length=50)
    provice = models.ForeignKey(ProveceDict)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 用户信息
class UserProfile(models.Model):
    avatar_url = models.CharField(u'头像地址', max_length=200)
    avatar_thumbnall_url = models.CharField(u'头像缩略图地址', max_length=200)
    nick_name = models.CharField(u'昵称', max_length=50)
    teacher_description = models.CharField(u'任课教师描述', max_length=200)
    qq_number = models.CharField(u'qq号', max_length=20)
    mobile = models.CharField(u'手机号', max_length=11)
    company_name = models.CharField(u'公司名称', max_length=150)
    position = models.CharField(u'地址', max_length=150)
    city = models.ForeignKey(CityDict)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s, %s，%s' % (self.nick_name, self.company_name, self.city)


# 证书
class Certificate(models.Model):
    name = models.CharField(u'证书名称', max_length=50, null=False)
    image_url = models.CharField(u'证书图片地址', max_length=200)

    class Meta:
        verbose_name = u'证书'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 徽章
class BadgeDict(models.Model):
    name = models.CharField(u'徽章名称', max_length=50, null=False)
    badge_url = models.CharField(u'徽章地址', max_length=200)

    class Meta:
        verbose_name = u'徽章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
