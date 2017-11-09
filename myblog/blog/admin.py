# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",'content','pub_time')
    #增加过滤器
    list_filter = ("pub_time",)
    # admin.site.register(Article)

admin.site.register(Article,ArticleAdmin)

