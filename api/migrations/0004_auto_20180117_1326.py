# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180117_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Setting'),
        ),
    ]
