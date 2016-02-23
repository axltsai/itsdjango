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

    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        Comment.objects.create(
            visitor = visitor,
            email = email,
            content = content,
            date_time = date_time,
            restaurant = r
        )
    return render_to_response('comments.html',
                              RequestContext(request,locals()))
