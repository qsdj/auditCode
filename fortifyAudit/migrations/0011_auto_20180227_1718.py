# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortifyAudit', '0010_vulnexplanation'),
    ]

    operations = [
        migrations.CreateModel(
            name='VulnDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('classId', models.CharField(max_length=255)),
                ('explanation', models.TextField(default=b'', null=True)),
                ('abstract', models.TextField(default=b'')),
                ('recommendations', models.TextField(default=b'')),
                ('references', models.TextField(default=b'')),
            ],
        ),
        migrations.DeleteModel(
            name='VulnExplanation',
        ),
    ]
