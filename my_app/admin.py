# -*- coding: utf-8 -*-
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from my_app.models import UserProfile, point_type, point, club
# Register your models here.
#class point_level_admin(admin.ModelAdmin)
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Профиль'

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

class point_type_admin(admin.ModelAdmin):
	list_display = ('name','procent','min_s')

class point_admin(admin.ModelAdmin):
	list_display = ('pid','fio','point_type','money')

#class club_admin(admin.ModelAdmin):
#	list_display = ('name','club_type')

class club_admin(admin.ModelAdmin):
	list_display = ('name','club_type','ipaddr')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(point_type,point_type_admin)
admin.site.register(point,point_admin)
admin.site.register(club,club_admin)


