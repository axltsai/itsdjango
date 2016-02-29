#coding:utf8
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from restaurants.models import Food, Restaurant, Comment
from django.utils import timezone
from django.template import RequestContext
from forms import CommentForm
from django.contrib.sessions.models import Session
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
    request.session['restaurant'] = restaurants

    sid = request.COOKIES['sessionid']
    sid2 = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + \
             'Session ID2:' + sid2 + \
             '<br>Expire_date:' + str(s.expire_date) + \
             '<br>Data:' + str(s.get_decoded())

    return render_to_response('restaurants_list.html', locals())

def comment(request,id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurant_list/")

    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            visitor = f.cleaned_data['visitor']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = timezone.localtime(timezone.now())
            c = Comment.objects.create(
                visitor = visitor,
                email = email,
                content = content,
                date_time = date_time,
                restaurant = r
            )
            f = CommentForm(initial = {'content':'沒意見'})
    else:
        f = CommentForm(initial = {'content':'沒意見'})

    return render_to_response('comments.html',
                              RequestContext(request,locals()))


def set_c(request):
    response = HttpResponse('set your lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('no cookies')

def use_session(request):
    request.session['lucky_number'] = 8   #設置 lucky_number
    if 'lucky_number' in request.session:
        #讀取 lucky_number
        lucky_number = request.session['lucky_number']
        response = HttpResponse('your lucky_number is ' + lucky_number)

    del request.session['lucky_number']

    return response

def session_test(request):
    sid = request.COOKIES['sessionid']
    sid2 = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + \
             'Session ID2:' + sid2 + \
             '<br>Expire_date:' + str(s.expire_date) + \
             '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)