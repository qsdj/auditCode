# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0012_fortifytaskvulns_taskvulnanalysisinfo_replacementdefinitions'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnAnalysisInfo_DefaultNode',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fortifytaskvulns',
            name='taskVulnAnalysisInfo_NodeRef',
            field=models.TextField(null=True),
        ),
    ]
