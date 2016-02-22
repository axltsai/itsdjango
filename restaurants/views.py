#coding:utf8
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from restaurants.models import Food, Restaurant
# Create your views here.

def menu(request):
    path = request.get_full_path()
    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id = request.GET['id'])
        return render_to_response('menu.html', locals())
    else:
        return HttpResponseRedirect('/restaurants_list/')



def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    path = request.get_full_path()
    return render_to_response('restaurants_list.html', locals())