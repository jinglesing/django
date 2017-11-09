# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default="Title")
    content = models.TextField(null=True)
    #创建对象同时设定当前时间
    pub_time = models.DateTimeField(null=True)
    #返回类的实例对象
    def __unicode__(self):
        return self.title