# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0004_fortifytasklog_taskcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FortifyTaskVulns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskId', models.CharField(max_length=50)),
                ('taskLogTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
