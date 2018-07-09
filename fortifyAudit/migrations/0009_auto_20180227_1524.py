# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0008_fortifytask_taskvulnoverview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortifytask',
            name='taskJavaClassPath',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskLoc',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskNumberOfFiles',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskResult',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskScanTime',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskSourceBasePath',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskSourceFiles',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskVulnCount',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskVulnOverview',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytasklog',
            name='taskComment',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnAnalysisInfo',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnAnalyzerName',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnClassId',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnClassInfo',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnDefaultSeverity',
            field=models.CharField(default=b'', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnKingdom',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetFile',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetId',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetLineEnd',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetLineStart',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetText',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnSubtype',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fortifytaskvulns',
            name='taskVulnType',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
    ]
