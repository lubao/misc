#Create your views here.
import subprocess
from django.core.context_processors import csrf
from django.http import HttpResponse
from django import template
from django.shortcuts import render_to_response
from django.template.loader import render_to_string

def search_form(request):
    if request.method == 'GET' :
        my_csrf = {}
        my_csrf.update(csrf(request))
        form_path = 'template/searchForm.html'
        return render_to_response (form_path, my_csrf)

def result_form(request):
    if request.method == 'POST':
        form_path = 'template/resulForm.html'
        HOME_PATH = "/home/paul/django_projects/genConfig"
        import os
        os.chdir(HOME_PATH)
        cmd = "./SumSearch/search.py {0} {1} {2} {3} {4} {5}".format(
                     request.POST['Model'],
                     request.POST['sYear'],
                     request.POST['eYear'],
                     request.POST['sPrice'],
                     request.POST['ePrice'],'SumSearch/final_data')
        #ret = os.popen(cmd).read()
        #print cmd

        ret = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        newret = [e for e in ret.stdout.readlines()[0].split("<p>") if e != ""]
        # newret = ret
        #print newret
        #print len(newret)

        #for i in newret:
        #    print i
        #print ret

        #print cmd
        #ret.replace('\\n','').replace('\\r','').replace('\\\'','\'').strip()
        #print os.popen('pwd').read()
        #print ret
        #ret = ret.split('***')
        userquery = "<b>Model</b>: %s" % (request.POST['Model'])
        return render_to_response (form_path, {
         'return' : newret,
         'userquery' : cmd,
         'model' : request.POST['Model'],
         'syear' : request.POST['sYear'],
         'eyear' : request.POST['eYear'],
         'sprice' : request.POST['sPrice'],
         'eprice' : request.POST['ePrice'],
         'csrf_token' : request.POST['csrfmiddlewaretoken']
          })
