#!/usr/bin/env python
#coding:utf8
#Created by axltsai on 2016/02/21 11:24

from django.http import HttpResponse
from django.template.loader import get_template
from django import template
from django.shortcuts import render_to_response

def here(request):
    return HttpResponse('hey,I am here! 中文測試！！')


def math(request,a,b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b

    # html = '''<html>sum={s}<br>dif={d}<br>
    #               pro={p}<br>quo={q}</html>'''.format(s=s,d=d,p=p,q=q)

    # with open('templates/math.html','r') as reader:
    #     t = template.Template(reader.read())

    # t = get_template('math.html')
    # c = template.Context({'s':s,
    #                       'd':d,
    #                       'p':p,
    #                       'q':q,
    #                       'a':a,
    #                       'b':b,
    #                       })
    # return HttpResponse(t.render(c))

    # from django.shortcuts import render_to_response 做了:get_template(),render(),HttpResponse() 三合一
    # locals() 自動將所有變數做成dictionary
    return render_to_response('math.html',locals())