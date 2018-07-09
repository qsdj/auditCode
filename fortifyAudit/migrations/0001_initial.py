# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fortifyTask',
            fields=[
                ('taskCreateTime', models.DateField(auto_created=True)),
                ('taskId', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('taskAddress', models.CharField(max_length=255)),
                ('taskDestroyTime', models.DateField()),
                ('taskResult', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='fortifyTaskLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskLogTime', models.DateField(auto_created=True)),
                ('taskId', models.CharField(max_length=50)),
                ('taskStatue', models.CharField(max_length=250)),
            ],
        ),
    ]
