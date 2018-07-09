#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from django.db import models


# Create your models here.
class FortifyTask(models.Model):
    # taskId 是任务ID 自动生成
    taskId = models.CharField(max_length=50, primary_key=True)
    taskAddress = models.CharField(max_length=255)
    # 保存gitlab的key
    # taskKey = models.TextField()
    taskCreateTime = models.DateTimeField(auto_now=True)  # 任务创建时间
    taskDestroyTime = models.DateTimeField(auto_now=True)  # 任务完成时间

    # ('build_id', 'number_of_files', 'loc', 'java_class_path', 'source_base_path', 'scan_time', 'source_files')
    taskBuildId = models.CharField(max_length=255, default="build_id")
    taskNumberOfFiles = models.TextField(default="", null=True)
    taskLoc = models.TextField(default="", null=True)
    taskJavaClassPath = models.TextField(default="", null=True)
    taskSourceBasePath = models.TextField(default="", null=True)
    taskScanTime = models.TextField(default="", null=True)
    taskSourceFiles = models.TextField(default="", null=True)

    taskVulnCount = models.TextField(default="", null=True)  # 用于存放项目的漏洞个数
    taskVulnOverview = models.TextField(default="", null=True)  # 漏洞概览json

    taskResult = models.TextField(default="", null=True)
    taskReportFPR = models.CharField(default="", null=True, max_length=200)
    taskReportPDF = models.CharField(default="", null=True, max_length=200)


class FortifyTaskLog(models.Model):
    """
    用于存储审计任务日志
    """
    taskId = models.CharField(max_length=50)
    taskLogTime = models.DateTimeField(auto_now=True)
    taskStatus = models.TextField(null=True)
    taskComment = models.TextField(default="", null=True)  # 用于记录程序输出信息
    taskStatusCode = models.TextField(null=True)
    """
    任务完成                 0
    拉去代码                 1
    任务拉取代码遇到异常       2
    完成代码拉取              3
    建立 fortify 扫描任务     4
    fortify扫描任务完成       5
    fortify未生成报告         6
    fortify转换pdf           7
    fortify扫描结果转换pdf成功 8
    fortify扫描结果转换pdf失败 9
    开始处理build信息         10
    开始处理vuln信息          11
    fortify vuln 处理遇到异常 12
    开始处理 Description 信息 13
    fortify 完成             0
    """


class FortifyTaskVulns(models.Model):
    """
    用于存储审计后的漏洞结果
    """
    taskId = models.CharField(max_length=50)
    taskLogTime = models.DateTimeField(auto_now=True)
    # OrderedDict([('class_id', '4C36222E-0455-451f-9D51-7B15E2B713FA'), ('kingdom', 'Encapsulation'),
    #              ('type', 'System Information Leak'), ('subtype', 'External'), ('analyzer_name', 'semantic'),
    #              ('default_severity', '3.0')])
    taskVulnClassInfo = models.TextField(default="", null=True)  # 存储class_info 完整信息，字典
    taskVulnClassId = models.CharField(max_length=255, default="", null=True)
    taskVulnKingdom = models.TextField(default="", null=True)
    taskVulnType = models.CharField(max_length=255, default="", null=True)  # 漏洞类型
    taskVulnSubtype = models.CharField(max_length=255, default="", null=True)
    taskVulnAnalyzerName = models.CharField(max_length=255, default="", null=True)  # 分析器名称
    taskVulnDefaultSeverity = models.CharField(max_length=10, default="", null=True)  # 严重等级分数
    # 'analysis_info', 'class_info', 'count', 'index',
    #  'instance_info']
    taskVulnAnalysisInfo = models.TextField(default="", null=True)  # 存储 analysis_info 完整信息，字典，会导致部分内部key丢失掉
    # {'replacement_defs': None, 
    # 'context': Context(function_name='md5sign', namespace='lib~^~payment~^~alipayapi~^~lib'
    # , enclosing_class='sign', decl_location=Location(path='lib/Payment/AliPayAPI/Lib/Sign.php', line_start='31', line_end='32', col_start='9', col_end='0')), 
    # 'trace': Trace(nodes=[Node(is_default=True, \
    # snippet_id='AA745D3DB840CD3BBBCAAFC1F9D796E5#lib/Payment/AliPayAPI/Lib/Sign.php:32:32', \
    # source_location=Location(path='lib/Payment/AliPayAPI/Lib/Sign.php', line_start='32', \
    # line_end='32', col_start='0', col_end='0'), 
    # action=TypeValue(type='InCall', value='md5()'), \
    # reason='3E15CC2F-6FD3-405F-BEF8-2F0E7B30945A', knowledge=[])], nodes_ref=[])}

    taskVulnAnalysisInfo_ReplacementDefinitions = models.TextField(null=True)
    # taskVulnAnalysisInfo_Trace = models.TextField(null=True)
    # list 是有序序列
    taskVulnAnalysisInfo_DefaultNode = models.TextField(null=True)  # 存储代码调用默认节点
    taskVulnAnalysisInfo_NodeRef = models.TextField(null=True)  # 存储代码调用节点
    # 在 nodes 里面是 list ，存储及提取时注意

    taskVulnSnippetId = models.CharField(max_length=255, default="", null=True)  # 对应的代码块

    taskVulnSnippetFile = models.CharField(max_length=255, default="", null=True)  # 对应文件
    taskVulnSnippetLineStart = models.CharField(max_length=255, default="", null=True)
    taskVulnSnippetLineEnd = models.CharField(max_length=255, default="", null=True)
    taskVulnSnippetText = models.TextField(default="", null=True)


class VulnDescription(models.Model):
    type = models.CharField(max_length=255, null=False)
    classId = models.CharField(max_length=255, null=False)
    explanation = models.TextField(default="", null=True)
    abstract = models.TextField(default="", null=False)
    recommendations = models.TextField(default="", null=False)
    references = models.TextField(default="", null=False)
