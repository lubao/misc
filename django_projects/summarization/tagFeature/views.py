# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponse
from django import template
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from summarization.tagFeature.models import Advertise
from django.utils import simplejson

def ajax_save(request):
    record_id = request.POST.get('id')
    content = request.POST.get('content')
    cur_ad = Advertise.objects.get(id=record_id)
    cur_ad.marked = 1
    cur_ad.content = content
    cur_ad.save()
    return
 
def tag_feature (request):
   ajax_next = False
   if request.is_ajax():
        act = request.POST.get('act')
        if (act == 'save'):
           ajax_save(request)
           return HttpResponse(simplejson.dumps({}), 
                 mimetype='application/javascript')
        elif (act == 'next'):
           ajax_save(request)
           ajax_next = True

   if request.method == 'GET' or ajax_next == True :
        working_advertise = Advertise.objects.filter(marked=0)[0]
        context = { 'id' : working_advertise.id, 
              'content' : working_advertise.content, }
        if ajax_next == True :
            return HttpResponse(simplejson.dumps(context), 
                 mimetype='application/javascript')
        context.update(csrf(request))
        mark_editor_path = 'template/editor.html'
        return render_to_response (mark_editor_path, context)
