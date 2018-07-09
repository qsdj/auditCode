# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0003_auto_20180124_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortifytasklog',
            name='taskComment',
            field=models.TextField(default=b''),
        ),
    ]
