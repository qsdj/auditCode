# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0005_fortifytaskvulns'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortifytask',
            name='taskBuildId',
            field=models.CharField(default=b'build_id', max_length=255),
        ),
        migrations.AddField(
            model_name='fortifytask',
            name='taskJavaClassPath',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytask',
            name='taskLoc',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytask',
            name='taskNumberOfFiles',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytask',
            name='taskScanTime',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytask',
            name='taskSourceBasePath',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='fortifytask',
            name='taskSourceFiles',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskResult',
            field=models.TextField(default=b''),
        ),
    ]
