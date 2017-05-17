# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 10:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('1', 'Todo'), ('2', 'Doing'), ('3', 'Done')], max_length=1)),
                ('updated', models.DateTimeField(default=datetime.datetime(2017, 5, 15, 10, 26, 33, 293000, tzinfo=utc))),
            ],
        ),
    ]