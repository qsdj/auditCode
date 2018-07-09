# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0009_auto_20180227_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='VulnExplanation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('explanation', models.TextField(default=b'', null=True)),
            ],
        ),
    ]
