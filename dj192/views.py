#!/usr/bin/env python
#coding:utf8
#Created by axltsai on 2016/02/21 11:24

from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect,RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def math(request,a,b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b


    # from django.shortcuts import render_to_response 做了:get_template(),render(),HttpResponse() 三合一
    # locals() 自動將所有變數做成dictionary
    return render_to_response('math.html',locals())

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome! ' +request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())

def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username','')
    password = request.POST.get('password','')

    user = auth.authenticate(username=username,password=password)

    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html',
                                  RequestContext(request,locals()))

def index(request):
    return render_to_response('index.html',
                              RequestContext(request, locals()))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',
                              RequestContext(request,locals()))
