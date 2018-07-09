# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0011_auto_20180227_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnAnalysisInfo_ReplacementDefinitions',
            field=models.TextField(null=True),
        ),
    ]
