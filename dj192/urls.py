#coding:utf8
"""dj192 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from views import math,welcome,index,register#,login
from restaurants.views import menu,list_restaurants,comment
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
    url(r'^menu/(\d{1,5})/$', menu),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^accounts/login/$', login, {'template_name':'login.html'}), #指定使用哪一個template
    url(r'^accounts/logout/$', logout, {'template_name':'logout.html'}),
    url(r'^index/$', index),
    url(r'^accounts/register/$', register),


]
