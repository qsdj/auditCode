#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import binascii
import json
import os
import urllib2

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.shortcuts import render

from models import FortifyTask
from models import FortifyTaskLog
from tasks import createTask as fortifyCreateTask


def hexdecode(value):
    """
    Decodes string value from hex to plain format

    >>> hexdecode('666f6f626172')
    'foobar'
    """

    value = value.lower()
    return (value[2:] if value.startswith("0x") else value).decode("hex")


def hexencode(value):
    """
    Encodes string value from plain to hex format

    >>> hexencode('foobar')
    '666f6f626172'
    """

    # return utf8encode(value).encode("hex")
    return value.encode("hex")


# Create your views here.
@csrf_exempt
# https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/#django.views.decorators.csrf.csrf_exempt
def createTask(request):
    """

    :param request:
    :return:
    """

    """
POST /createTask HTTP/1.1
Host: 127.0.0.1:8001
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 4442

key=base64key&addr=git@git.xxx.com:xxxx/xxxx.git
    
    
    # 使用GUI客户端时使用的命令行   
    "-b"
    "git.xxxxxx.com_xxxxxx_gametopic"
    "-machine-output"
    "-format"
    "fpr"
    "-f"
    "C:\Users\c4bbage\AppData\Local/Fortify\AWB-16.10\git.xxxxxx.com_xxxxxx_gametopic\git.xxxxxx.com_xxxxxx_gametopic.fpr"
    "-no-default-rules"
    "-rules"
    "C:\Program Files\HP_Fortify\HP_Fortify_SCA_and_Apps_16.10\Core\config\rules\core_sql.bin"
    "-rules"
    "C:\Program Files\HP_Fortify\HP_Fortify_SCA_and_Apps_16.10\Core\config\rules\core_php.bin"
    "-rules"
    "C:\Program Files\HP_Fortify\HP_Fortify_SCA_and_Apps_16.10\Core\config\rules\extended_content.bin"
    "-rules"
    "C:\Program Files\HP_Fortify\HP_Fortify_SCA_and_Apps_16.10\Core\config\rules\extended_config.bin"
    """
    resp = {
        'taskId': "",
        'status': "创建中",
        "code": 0
    }
    gitKey = ""
    gitAddress = ""

    try:
        gitKey = request.POST['key'].strip()
        gitAddress = request.POST['addr'].strip()
    except Exception, e:
        print e.message
        pass
    try:
        gitKey = binascii.a2b_base64(urllib2.unquote(gitKey))
    except Exception, e:
        resp['status'] = u'key 非标准格式'
        return HttpResponse(json.dumps(resp), content_type="application/json")
    taskId = hexencode(os.urandom(8))
    resp['taskId'] = taskId
    # 存储任务
    fortifyTask = FortifyTask(taskId=taskId, taskAddress=gitAddress)
    fortifyTask.save()

    ret = fortifyCreateTask.delay(taskId=taskId, gitKey=gitKey, gitAddress=gitAddress)
    # print "[-]", "celery ID", ret
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def view(request):
    """
    任务简要信息
    :param request:
    :return:
    """
    taskId = request.POST['taskId']
    resp = {
        "taskId": "",  # 任务ID
        "status": "",  # 状态 taskStatus
        "code": 0,     # 状态码
        "data": ""     # 用于详情
    }
    task = FortifyTask.objects.values("taskId", "taskCreateTime", "taskAddress").get(taskId=taskId)
    print task

    # print json.dumps(task.__dict__)
    # print task.taskBuildId
    # print connection.queries[-1]['sql']
    taskLog = FortifyTaskLog.objects.order_by("-taskLogTime").filter(taskId=taskId).all()
    print connection.queries[-1]['sql']
    taskEndLog = taskLog.first()
    resp['code'] = taskEndLog.taskStatusCode
    resp['status'] = taskEndLog.taskStatus

    # for i in taskLog:
    #     print i.taskStatusCode
    # resp['code'] = taskLog.first().taskStatusCode

    if task:
        resp['taskId'] = taskId
        return HttpResponse(json.dumps(resp, indent=4), content_type="application/json")
    else:
        resp['taskId'] = taskId
        return HttpResponse(json.dumps(resp, indent=4), content_type="application/json")


@csrf_exempt
def viewPdf(request):
    # if request.method is 'GET':
    #     return HttpResponse("ERROR")
    return render(request,"taskview.html")


@csrf_exempt
def viewLog(request):
    taskId = request.GET['taskId']
    fortifyTask.objects.filter(taskId=taskId).get()
    pass


@csrf_exempt
def viewFpr(request):
    pass
