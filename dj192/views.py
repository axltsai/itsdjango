#!/usr/bin/env python
#coding:utf8
#Created by axltsai on 2016/02/21 11:24

from django.http import HttpResponse
from django.shortcuts import render_to_response

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

def menu(request):
    foods = [
        {
            'name' : '炒蛋',
            'price' : 60,
            'comment' : 'yummy',
            'is_spicy' : False
        },
        {
            'name' : '魯肉飯',
            'price' : 50,
            'comment' : '油多',
            'is_spicy' : False
        },
    ]

    return render_to_response('menu.html',locals())