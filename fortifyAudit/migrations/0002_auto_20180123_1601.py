# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortifytask',
            name='taskCreateTime',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fortifytasklog',
            name='taskLogTime',
            field=models.DateField(auto_now=True),
        ),
    ]
