#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: c4bbage@qq.com
"""auditCode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from  fortifyAudit import views as fortifyViews

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^createTask', fortifyViews.createTask, name="fortifyCreate"),
    url(r'^viewTask$', fortifyViews.view, name="fortifyView"),            # 查看结果
    url(r'^viewTask/pdf$', fortifyViews.viewPdf, name="fortifyViewPdf"),  # 下载PDF文件
    url(r'^viewTask/fpr$', fortifyViews.viewFpr, name="fortifyViewFpr")   # 下载PDF文件

]
