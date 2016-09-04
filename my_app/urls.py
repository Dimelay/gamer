from django.conf.urls import url
from . import views

from django.contrib import admin
urlpatterns = [
url(r'^login/$', views.user_login, name='login'),
url(r'^logout/$', views.user_logout, name='logout'),
url(r'^$', views.index, name='index'),
url(r'^admin/', admin.site.urls),
]
