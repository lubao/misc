# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
import datetime
from time import localtime
from pytz import timezone
from time import strftime
TIME_ZONE = [('#est_time','US/Eastern'),
             ('#pst_time','US/Pacific'),
             ('#mst_time','US/Mountain'),
             ('#cst_time','US/Central')]
UTC = timezone('UTC') 
CST = timezone('US/Central') 
TIME_FMT = '%Y-%m-%d %H:%M:%S %Z%z'
def get_time():
    ret = []
    for tz in TIME_ZONE:
        local_time=CST.localize(
            datetime.datetime.now()).astimezone(
            timezone(tz[1])).strftime(TIME_FMT)
        ret.append({'id':tz[0],'time':local_time})
    ret.append({'id':'#system_time',
               'time': strftime("%a, %d %b %Y %H:%M:%S %Z%z", localtime())})
    return simplejson.dumps(ret)
#        [   
#            {'id':'#system_time',
#            'time': strftime("%a, %d %b %Y %H:%M:%S", localtime())},
#            {'id':'#pst_time',
#            'time': strftime("%a, %d %b %Y %H:%M:%S", localtime())},
#            {'id':'#mst_time',
#            'time': strftime("%a, %d %b %Y %H:%M:%S", localtime())},
#            {'id':'#cst_time',
#            'time': strftime("%a, %d %b %Y %H:%M:%S", localtime())},
#            {'id':'#est_time',
#            'time': strftime("%a, %d %b %Y %H:%M:%S", localtime())},
#        ]
#    )

def home(request):
    if request.is_ajax():
        return HttpResponse(
                get_time(), mimetype='application/javascript')
    context = {
        'system_time':strftime("%a, %d %b %Y %H:%M:%S %Z%z", localtime()) }
    context.update(csrf(request))
    return render_to_response(
        'AjaxClock/clock.html', context)
