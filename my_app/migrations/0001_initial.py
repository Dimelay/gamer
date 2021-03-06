# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 09:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0443\u0431\u0430')),
                ('club_type', models.CharField(choices=[('0', '\u041f\u0443\u043d\u043a\u0442 \u043f\u0440\u0438\u0435\u043c\u0430'), ('1', '\u041f\u0443\u043d\u043a \u0432\u044b\u0434\u0430\u0447\u0438')], default='0', max_length=1, verbose_name='\u0422\u0438\u043f \u043a\u043b\u0443\u0431\u0430')),
                ('ipaddr', models.GenericIPAddressField(verbose_name='IP \u043a\u043b\u0443\u0431\u0430')),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0443\u0431',
                'verbose_name_plural': '\u041a\u043b\u0443\u0431\u044b',
            },
        ),
        migrations.CreateModel(
            name='point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=40, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440')),
                ('money', models.BigIntegerField(default=0, verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441')),
                ('active', models.CharField(choices=[('0', '\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u0435\u043d'), ('1', '\u0410\u043a\u0442\u0438\u0432\u0435\u043d')], default='1', max_length=1, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0430\u043a\u0442\u0438\u0432\u0435\u043d')),
                ('last_date', models.DateTimeField(default=datetime.datetime(2016, 8, 26, 12, 28, 42, 252001), verbose_name='\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c')),
                ('passport_serial', models.CharField(blank=True, default='', max_length=6, verbose_name='\u041f\u0430\u0441\u043f\u043e\u0440\u0442 \u0441\u0435\u0440\u0438\u044f')),
                ('passport_number', models.CharField(blank=True, default='', max_length=7, verbose_name='\u041f\u0430\u0441\u043f\u043e\u0440\u0442 \u043d\u043e\u043c\u0435\u0440')),
                ('dogovor', models.CharField(blank=True, default='', max_length=15, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430')),
                ('fio', models.CharField(blank=True, default='', max_length=200, verbose_name='\u0424\u0418\u041e')),
                ('phone', models.CharField(blank=True, default='', max_length=12, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')),
                ('friend', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.point', verbose_name='\u0414\u0440\u0443\u0433')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0430',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='point_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('procent', models.IntegerField(verbose_name='\u043f\u0440\u043e\u0446\u0435\u043d\u0442')),
                ('min_s', models.IntegerField(verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0421\u0442\u0430\u0432\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u041a\u0430\u0440\u0442\u044b',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u041a\u0430\u0440\u0442',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u043e\u0442\u043e\u0432\u043e\u0433\u043e')),
                ('level', models.CharField(choices=[('0', '\u041e\u0431\u044b\u0447\u043d\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'), ('1', '\u0423\u043f\u0440\u0430\u0432\u043b\u044f\u044e\u0449\u0438\u0439')], default='0', max_length=1, verbose_name='\u041f\u0440\u0430\u0432\u0430')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='point_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.point_type', verbose_name='\u0422\u0438\u043f \u043a\u0430\u0440\u0442\u044b'),
        ),
    ]
