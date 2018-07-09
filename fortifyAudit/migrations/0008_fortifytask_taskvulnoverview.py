# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0007_auto_20180226_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortifytask',
            name='taskVulnOverview',
            field=models.TextField(default=b''),
        ),
    ]
