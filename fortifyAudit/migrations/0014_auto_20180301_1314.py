# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0013_auto_20180228_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortifytasklog',
            name='taskStatue',
            field=models.TextField(null=True),
        ),
    ]
