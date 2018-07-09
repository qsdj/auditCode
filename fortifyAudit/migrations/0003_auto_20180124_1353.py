# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0002_auto_20180123_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortifytask',
            name='taskCreateTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fortifytask',
            name='taskDestroyTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fortifytasklog',
            name='taskLogTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
