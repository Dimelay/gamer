# -*- coding: utf-8 -*-
from django import forms

class SearchPoint(forms.Form):

	class Media:
		js = ('js/searchpoint.js',)
	pid = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'autofocus':'on',
		'onkeypress':"if(event.charCode == 64 || event.charCode == 34) $('#form_searchpoint').trigger('submit');"
		}),
		label='Поиск клиента', max_length=100)