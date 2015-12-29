'''
Created on Jun 28, 2015

@author: chamishr
'''
from django.http import HttpResponse , Http404
import datetime
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello to world Of Django and Python web dev")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Current Time and Date is %s</body></html>" % now
    return HttpResponse(html)
#offset example
def current_datetime_offset(request, offset):
    try :
        offset= (int)(offset)
    except ValueError :
        raise Http404()
        
    now = datetime.datetime.now() - datetime.timedelta(hours=offset)
    html ="<html><body>Time after %d offset is %s</body></html>" % (offset,now)
    return HttpResponse(html)

# using template
from django.template.loader import get_template
from django.template import Context

def current_datetime_template(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

# using shortcut
def current_datetime_template_sortcut(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', Context({'current_date':now }))