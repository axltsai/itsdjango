#coding:utf8
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from restaurants.models import Food, Restaurant, Comment
from django.utils import timezone
from django.template import RequestContext
# Create your views here.

def menu(request,id):
    path = request.get_full_path()
    # if 'id' in request.GET and request.GET['id'] != '':
    #     restaurant = Restaurant.objects.get(id = request.GET['id'])
    #     return render_to_response('menu.html', locals())
    if id:
        restaurant = Restaurant.objects.get(id=id)
        return render_to_response('menu.html', locals())
    else:
        return HttpResponseRedirect('/restaurants_list/')



def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    path = request.get_full_path()
    return render_to_response('restaurants_list.html', locals())

def comment(request,id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurant_list/")
    error = True
    errors = []
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        # error = any(not request.POST[k] for k in request.POST)  #檢查每個欄位都要有值
        if any(not request.POST[k] for k in request.POST):
            errors.append('* 有空白欄位,請不要留空')
        if '@' not in email:
            # error = True
            errors.append('* email 格式不正確,請重新輸入')
        if not errors:
            Comment.objects.create(
                visitor = visitor,
                email = email,
                content = content,
                date_time = date_time,
                restaurant = r
            )
            visitor,email,content = ('','','')
    return render_to_response('comments.html',
                              RequestContext(request,locals()))
