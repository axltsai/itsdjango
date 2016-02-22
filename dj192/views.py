#!/usr/bin/env python
#coding:utf8
#Created by axltsai on 2016/02/21 11:24

from django.shortcuts import render_to_response,HttpResponse

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