# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0006_auto_20180223_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortifytask',
            name='taskVulnCount',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnAnalysisInfo',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnAnalyzerName',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnClassId',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnClassInfo',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnDefaultSeverity',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnKingdom',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetFile',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetId',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetLineEnd',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetLineStart',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnSnippetText',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnSubtype',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnType',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
