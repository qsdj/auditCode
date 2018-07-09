# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0014_auto_20180301_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fortifytasklog',
            old_name='taskStatue',
            new_name='taskStatus',
        ),
        migrations.AddField(
            model_name='fortifytasklog',
            name='taskStatusCode',
            field=models.TextField(null=True),
        ),
    ]
