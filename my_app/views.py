# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse,render, redirect
#from django.template import loader, Context, RequestContext

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from my_app.models import club,  UserProfile, point
from my_app.forms import SearchPoint
#from django.views.decorators import csrf
#from django.views.decorators.csrf import csrf_protect
# Create your views here.

def user_login(request):
	if request.method == 'POST':
		auth_form = AuthenticationForm(request, data=request.POST)
		c = club.objects.filter(ipaddr=request.META["REMOTE_ADDR"]).count()
		if c <= 0:
			auth_form.add_error(None,'Неизвестное место....')
			return render(request,'login2.html',{'auth_form':auth_form})
		if auth_form.is_valid():
			#print auth_form.cleaned_data.get("username")
			#a=auth_form.clean()
			#print 'ADM %s' % auth_form.cleaned_data["password"]
			#user = authenticate(username=auth_form.username, password=auth_form.password)
			##u = UserProfile.objects.get(user=auth_form.get_user())
			##print u.phone
			login(request,auth_form.get_user())
			request.session['club_type'] = club.objects.values('club_type').get(ipaddr=request.META["REMOTE_ADDR"])['club_type']
			#request.session['club_type'] = club.objects.values('club_type').get(ipaddr=request.META["REMOTE_ADDR"])['club_type']
			return redirect("/")
		else:
			#print 'Not valid'
			#print auth_form.error_messages
			return render(request,'login2.html',{'auth_form':auth_form})
			#for i in auth_form.error_messages:
			#	print i, auth_form.error_messages[i]
		#if user is not None:
		#	if user.is_active:
		#		login(request,user)
		#		messages.add_message(request, messages.INFO, 'Hello world.')
			#return redirect("/")
		#	else:
		#		messages.add_message(request, messages.ERROR, 'User is not active')
		#else:
		#	messages.add_message(request, messages.ERROR, 'Password or username')
	else:
		auth_form = AuthenticationForm(None,None)
		return render(request,'login2.html',{'auth_form':auth_form})

@login_required(redirect_field_name=None)
def user_logout(request):
	logout(request)
	return redirect("/")

@login_required(redirect_field_name=None)
def index(request):
	searchpoint = SearchPoint()
	return render(request,"main.html",{'searchpoint':searchpoint})

@login_required(redirect_field_name=None)
@permission_required('point.point_all_view',raise_exception=True)
def cart(request):
    return render(request,"cart.html",{'point': point.objects.exclude(fio='').order_by('fio') })
