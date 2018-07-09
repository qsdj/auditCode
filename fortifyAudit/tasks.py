#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-29 09:37:48
# @Author  : c4bbage@qq.com
# @Link    : http://xxxxx.ooooo
# @Version : $Id$

from __future__ import absolute_import

"""
https://github.com/snehakokil/sonar-fortify
https://github.com/SonarQubeCommunity/sonar-fortify
https://github.com/abnamrocoesd/sonarqube-fortify-plugin

https://github.com/jaxley/python-fortify
https://github.com/tan9/fortify-issue-suppressor
https://github.com/liuna-liuna/ScmEnvConfig/blob/b6cd53708f3d35c10cae92e3cc6f2683047507df/fortify_usage_and_config.txt
"""

"""
fortify Scan and report from command line
https://community.softwaregrp.com/t5/Fortify-Discussions/Scan-and-report-from-command-line/td-p/1566021
"""

# 主要是命令行下的简单使用及结果上传
"""
https://github.com/mharlos/FortifyPythonScripts/blob/master/fortify.py
https://github.com/moloch--/Fortify-XML-Converter
"""

# https://github.com/EricRohlfs/FortifyCompare

import os
import time
import json
from subprocess import Popen, PIPE

from celery import shared_task
from gittle import Gittle

from auditCode.settings import BASE_DIR
from auditCode.settings import FORTIFY_BIN
from auditCode.settings import ReportGenerator_BIN
from .models import FortifyTaskLog
from .models import FortifyTask
from .models import FortifyTaskVulns
from .models import VulnDescription


def fortifyLogMsg(taskId, msg, comment="", code="1"):
    """
    记录任务操作细则到数据库
    :param taskId:任务ID
    :param msg:操作信息 taskStatue
    :param comment: taskComment
    :return:
    """
    print "[-] %s  taskId: %s  msg: %s" % (time.ctime(), taskId, msg)
    fortifyLog = FortifyTaskLog(taskId=taskId, taskStatus=msg, taskComment=comment, taskLogTime=time.ctime(),
                                taskStatusCode=code)
    fortifyLog.save()


@shared_task
def createTask(taskId, gitKey, gitAddress):
    """
    fortify 命令行调用
    fortify 使用手册 HPE_SCA_Guide_16.20.pdf
    :param taskId:
    :param gitKey:
    :param gitAddress:
    :return:
    """
    clonePath = os.path.join(BASE_DIR, "gitClone")
    outputPath = os.path.join(BASE_DIR, "reports")
    if not os.path.exists(clonePath):
        os.mkdir(clonePath)
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
    fortifyLogMsg(taskId=taskId, msg=u"拉取代码" + gitAddress, code=1)

    localPath = gitAddress.replace("http://", "").replace("https://", "").replace("/", "_").split("?")[0]
    localPath = localPath.replace("git@", "").replace(":", "_").replace(".git", "")
    localPath = os.path.join(clonePath, localPath)

    buildName = "_".join(localPath.split("_")[1:])

    try:
        if gitKey and gitAddress:
            from gittle.auth import GittleAuth
            # https://github.com/FriendCode/gittle/issues/18
            authkey = GittleAuth(pkey=gitKey)
            if not os.path.exists(localPath):
                Gittle.clone(gitAddress, local_path=localPath, auth=authkey)
            else:
                repo = Gittle(localPath, origin_uri=gitAddress, auth=authkey)
                repo.pull()
        else:
            if not os.path.exists(localPath):
                Gittle.clone(gitAddress, localPath)
            else:
                repo = Gittle(localPath, gitAddress)
                repo.pull()
    except Exception, e:
        # raise e
        fortifyLogMsg(taskId, u"任务拉取代码遇到异常" + str(e.message), "", code=2)
        return ""  # 结束任务
    fortifyLogMsg(taskId, u"完成代码拉取", "", code=3)

    fortifyBuild = Popen([FORTIFY_BIN, "-b", buildName, localPath], shell=True, stdout=PIPE, stderr=PIPE,
                         env=os.environ)
    stdout, stderr = fortifyBuild.communicate()
    print stderr
    fortifyLogMsg(taskId, u"建立 fortify 扫描任务" + buildName, stdout, code=4)
    # stdout 终端输出处理

    # outputFile 审计结果fpr
    outputFile = os.path.join(outputPath, "fpr", buildName) + ".fpr"

    fortifyScan = Popen([FORTIFY_BIN, "-b",
                         buildName, "-scan", "-exclude", "/**/*.js", "-format", "fpr", "-f", outputFile],
                        shell=True,
                        stdout=PIPE, stderr=PIPE, env=os.environ)
    # sourceanalyzer -b xxxxxx_appxxxxxx -show-build-warnings
    stdout, stderr = fortifyScan.communicate()
    # outputFile = "D:\\workspace\\auditCode\\reports\\fpr\\xxxxxx_gametopic.fpr"
    if os.path.isfile(outputFile):
        FortifyTask.objects.filter(taskId=taskId).update(taskReportFPR=outputFile)
        fortifyLogMsg(taskId, u"fortify扫描任务完成" + outputFile, stdout, code=5)
        # 报告处理方式
        # C:\Program Files\HP_Fortify\HP_Fortify_SCA_and_Apps_16.10\bin\ReportGenerator.bat
        # ReportGenerator -format pdf -f LegacyReport.pdf -source scan.fpr -template DeveloperWorkbook.xml \
        # -showSuppressed -showHidden
        # C:\Program Files\HP_Fortify\HP_Fortify_SCA_and_Apps_16.10\bin\BIRTReportGenerator.cmd
        outputPDF = os.path.join(outputPath, "pdf", buildName) + ".pdf"
        # 转换pdf
        fortifyLogMsg(taskId, u"fortify转换pdf" + outputPDF, stdout)
        reportGenerator = Popen(
            [ReportGenerator_BIN, "-format", "pdf", "-f", outputPDF, "-source", outputFile, "-template",
             "DeveloperWorkbook.xml", "-showSuppressed", "-showHidden"], shell=True, stdout=PIPE, stderr=PIPE,
            env=os.environ)
        stdout, stderr = reportGenerator.communicate()
        if os.path.exists(outputPDF):
            # 转换 pdf 成功后存储
            FortifyTask.objects.filter(taskId=taskId).update(taskReportPDF=outputPDF)
            fortifyLogMsg(taskId, u"fortify扫描结果转换pdf成功" + outputPDF, stdout)
        else:
            fortifyLogMsg(taskId, u"fortify扫描结果转换pdf失败" + outputPDF, stdout)
        # 解析fpr
        # 解析fpr,对所需要信息进行入库整理
        # 所有的属性不可重置
        from fortifyAudit import fortipy
        with fortipy.FPR(outputFile) as fpr:
            # fpr 属性
            # build', 'called_with_no_def', 'close','descriptions', 'engine_data',
            # 'files', 'get_code_for', 'get_types_of_vulns', 'get_vulns_of_type', 'snippets',
            # 'temppath', 'vulnerabilities'
            # 开始处理build信息
            # # 处理build中的loc
            fortifyLogMsg(taskId, u"开始处理build信息" + outputFile, "", code=7)
            newloc = []
            for loc in fpr.build.loc:
                newloc.append({loc.type: loc.value})
            # 处理build中的source_files
            newfiles = []
            for f in fpr.build.source_files:
                newfiles.append(dict(f._asdict()))
            if fpr.build.scan_time is None:
                scanTime = ""
            else:
                scanTime = fpr.build.scan_time
            FortifyTask.objects.filter(taskId=taskId).update( \
                taskBuildId=buildName, taskNumberOfFiles=fpr.build.number_of_files, \
                taskLoc=newloc.__str__(), taskJavaClassPath=fpr.build.java_class_path, \
                taskSourceBasePath=fpr.build.source_base_path, taskScanTime=scanTime, \
                taskSourceFiles=newfiles.__str__(), taskVulnCount=fpr.vulnerabilities.__len__(), \
                taskVulnOverview=json.dumps(fpr.get_types_overview_of_vulns()))
            # 处理完成build信息
            fortifyLogMsg(taskId, u"开始处理vuln信息" + outputFile, "", code=8)

            # 开始处理vuln信息
            for vuln in fpr.vulnerabilities:
                try:
                    if vuln.class_info.subtype == None:
                        subtype = ""
                    else:
                        subtype = vuln.class_info.subtype
                    snippet = fpr.get_snippet_of_id(vuln.analysis_info.trace.nodes[0].snippet_id)[0]
                    # 处理analyzer_info中的 ReplacementDefinitions
                    replacementDefinitions = {}
                    if vuln.analysis_info.replacement_defs is not None:
                        for item in vuln.analysis_info.replacement_defs:
                            if item is None:
                                continue
                            if isinstance(item, list):
                                for i in item:
                                    replacementDefinitions[i.key] = i.value
                            else:
                                replacementDefinitions.update(dict(item._asdict()))
                    replacementDefinitions = json.dumps(replacementDefinitions)
                    # 处理完成 analyzer_info 中的 ReplacementDefinitions
                    # 处理漏洞代码调用过程node

                    # nodesRef
                    # nodesRef = {'id': ""} # 取消字典存储方式
                    nodesRef = ""
                    if vuln.analysis_info.trace.nodes_ref is not None:
                        nodesRef = ','.join([node_ref.id.__str__() for node_ref in vuln.analysis_info.trace.nodes_ref])

                    node = vuln.analysis_info.trace.nodes[0]._asdict()
                    if vuln.analysis_info.trace.nodes[0]._asdict().has_key("source_location"):
                        node['source_location'] = vuln.analysis_info.trace.nodes[0].source_location._asdict()
                    if vuln.analysis_info.trace.nodes[0]._asdict().has_key("action"):
                        if node['action'] is not None:
                            node['action'] = vuln.analysis_info.trace.nodes[0].action._asdict()
                    # for node in i.analysis_info.trace.nodes:
                    #     if node._asdict().has_key("source_location"):
                    #         nodes['source_location']=node.source_location._asdict()
                    #     if node._asdict().has_key("action"):
                    #         if nodes['action'] is not None:
                    #             nodes['action']=node.action._asdict()

                    fortifyTaskVulns = FortifyTaskVulns(taskId=taskId,
                                                        taskVulnClassInfo=dict(vuln.class_info._asdict()),
                                                        taskVulnClassId=vuln.class_info.class_id,
                                                        taskVulnKingdom=vuln.class_info.kingdom,
                                                        taskVulnType=vuln.class_info.type,
                                                        taskVulnSubtype=subtype,
                                                        taskVulnAnalyzerName=vuln.class_info.analyzer_name,
                                                        taskVulnDefaultSeverity=vuln.class_info.default_severity,
                                                        # analysis_info 内容不能完全转换为字典，暂未存入
                                                        taskVulnAnalysisInfo="",
                                                        taskVulnAnalysisInfo_ReplacementDefinitions=replacementDefinitions,
                                                        taskVulnAnalysisInfo_DefaultNode=json.dumps(node),
                                                        taskVulnAnalysisInfo_NodeRef=nodesRef,
                                                        taskVulnSnippetId=vuln.analysis_info.trace.nodes[0].snippet_id,
                                                        taskVulnSnippetFile=snippet.file,
                                                        taskVulnSnippetLineStart=snippet.line_start,
                                                        taskVulnSnippetLineEnd=snippet.line_end,
                                                        taskVulnSnippetText=snippet.text)
                    fortifyTaskVulns.save()
                except Exception, e:
                    fortifyLogMsg(taskId, u"fortify vuln 处理遇到异常" + e.message.__str__(), "", 12)

            fortifyLogMsg(taskId, u"开始处理 Description 信息" + outputFile, "", 13)
            for desc in fpr.descriptions:
                if not VulnDescription.objects.filter(classId=desc.class_id).exists():
                    vulnDescription = VulnDescription(classId=desc.class_id, explanation=desc.explanation,
                                                      recommendations=desc.recommendations,
                                                      type=desc.content_type, references="",  # desc.references
                                                      )
                    vulnDescription.save()
    else:

        fortifyLogMsg(taskId, u"fortify未生成报告" + outputFile, stderr, 6)
    fortifyLogMsg(taskId, u"fortify整体流程结束", "", 0)
