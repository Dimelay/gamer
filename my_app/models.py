# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
"""
class club(models.Model):
	class Meta:
		verbose_name_plural = 'Клубы'
		verbose_name = 'Клуб'

	def __unicode__(self):
		return self.club_type.name

	club_type = models.ForeignKey('club_type',verbose_name='Название клуба')
	ipaddr = models.GenericIPAddressField(verbose_name='IP клуба')

class club_type (models.Model):
	class Meta:
		verbose_name_plural = 'Типы Клубов'
		verbose_name = 'Тип Клубов'

	def __unicode__(self):
		return self.name

	club_ch = (
		('0','Пункт приема'),
		('1', 'Пунк выдачи'),
		)
	name = models.CharField(max_length=50, verbose_name='Название клуба')
	club_type = models.CharField(max_length=1,verbose_name='Тип клуба',choices=club_ch,default='0')
"""
class club (models.Model):
	class Meta:
		verbose_name_plural = 'Клубы'
		verbose_name = 'Клуб'

	def __unicode__(self):
		return self.name

	club_ch = (
		('0','Пункт приема'),
		('1', 'Пунк выдачи'),
		)
	
	name = models.CharField(max_length=50, verbose_name='Название клуба',default='')
	club_type = models.CharField(max_length=1,verbose_name='Тип клуба',choices=club_ch,default='0')
	ipaddr = models.GenericIPAddressField(verbose_name='IP клуба')

class point_type(models.Model):
	class Meta:
		verbose_name_plural = 'Типы Карт'
		verbose_name = 'Тип Карты'

	def __unicode__(self):
		return self.name
	
	name = models.CharField(max_length=80,verbose_name='Название')
	procent = models.IntegerField(verbose_name='процент')
	min_s = models.IntegerField(verbose_name='Минимальная Ставка')

class point(models.Model):
    class Meta:
        permissions = (
            ('point_all_view','Список всех карт'),
        )
        verbose_name_plural = 'Карты'
        verbose_name = 'Карту'

    def __unicode__(self):
        return self.fio
    
    active_ch = (
		('0', 'Неактивен'),
		('1', 'Активен'),
		)
    pid = models.CharField(max_length=40,verbose_name='Идентификатор')
    money = models.BigIntegerField(verbose_name='Баланс',default=0)
    active = models.CharField(max_length=1, default='1', choices=active_ch, verbose_name='Пользователь активен' )
    last_date = models.DateTimeField(verbose_name='Последняя активность', default=datetime.datetime.now())
    passport = models.CharField(blank=True,max_length=15,verbose_name='Паспорт',default='')
    #passport_serial = models.CharField(blank=True,max_length=6,verbose_name='Паспорт серия',default='')
    #passport_number = models.CharField(blank=True,max_length=7,verbose_name='Паспорт номер',default='')
    point_type = models.ForeignKey('point_type',verbose_name='Тип карты', default=None,null=True, blank=True,on_delete=models.SET_NULL)
    dogovor = models.CharField(blank=True,max_length=15, default='',verbose_name='Номер договора')
    fio = models.CharField(max_length=200,blank=True,default='',verbose_name='ФИО')
    phone = models.CharField(blank=True,max_length=12,default='',verbose_name='Номер телефона')
    friend = models.ForeignKey('self',default='',verbose_name='Друг',null=True,blank=True)


class UserProfile(models.Model):
    
    user_level = (
    ('0', 'Обычный пользователь'),
    ('1', 'Управляющий'),
    )
    user = models.OneToOneField(User, related_name='profile')
    phone = models.CharField(max_length=12,blank=True,verbose_name='Номер сотового')
    level = models.CharField(max_length=1, choices=user_level, default='0', verbose_name='Права')

