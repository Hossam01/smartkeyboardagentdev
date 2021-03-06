# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='email',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='language',
            field=models.CharField(default='English', max_length=45),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_ip',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='register_ip',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
