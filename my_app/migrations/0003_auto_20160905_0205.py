# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 18:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20160904_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 5, 2, 5, 31, 155405), verbose_name='\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c'),
        ),
    ]
