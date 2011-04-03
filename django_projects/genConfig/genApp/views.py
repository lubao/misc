# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponse
from django import template
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
# from BeautifulSoup import BeautifulSoup
# import re

def show_app_form(request):
    if request.method == 'GET' :
        my_csrf = {}
        my_csrf.update(csrf(request))
        app_form_path = 'template/appForm.html'
        return render_to_response (app_form_path, my_csrf)

def gen_app_form(request):
    if request.method == 'POST' :
        num_of_schemas = 0
        current_schema_id = 0
        app_dict = {}
        data_list = request.raw_post_data.replace('+',' ').split("&")
        csrf_token = data_list.pop(0)
        app_dict['appId'] = data_list.pop(0).split("=")[1]
        app_dict['appName'] = data_list.pop(0).split("=")[1]
        app_dict['schemas'] = []
        while data_list :
            data = data_list.pop(0).split("=")
            num_of_fields = 0
            num_of_schemas += 1
            current_schema = {'schemaName':data[1] , 
              'schemaId':num_of_schemas,'fields':[], 
              'numOfFields':num_of_fields,}
            while data_list and not data_list[1].startswith('schemaName'): 
                hasChoice = False
                field_name = data_list.pop(0).split("=")[1]
                field_type = data_list.pop(0).split("=")[1]
                if field_type == 'Integer':
                    field_range = int(data_list.pop(0).split("=")[1])
                elif field_type == 'String':
                    field_range = 0
                elif field_type == 'Date Time':
                    field_range = -1
                elif field_type == 'Single Choice':
                    field_range = -3
                    hasChoice = True
                else: # field_type == 'Multiple+Choice':
                    field_range = -2
                    hasChoice = True
                if hasChoice == True :
                    choices = []
                    while data_list and data_list[0].startswith('choice'):
                        choices.append(data_list.pop(0).split('=')[1])
                    current_schema['fields'].append({
                    'fieldId':num_of_fields,
                    'fieldName':field_name, 
                    'fieldRange':field_range,
                    'numOfChoices':len(choices), 
                    'choices':choices,})
                else:    
                    current_schema['fields'].append({
                        'fieldId':num_of_fields,
                        'fieldName':field_name, 
                        'fieldRange':field_range,})
                num_of_fields += 1
            current_schema['numOfFields'] = num_of_fields
            app_dict['schemas'].append(current_schema)
        app_dict['numOfSchemas'] = num_of_schemas
        doc = render_to_string ('template/app_description.xml',app_dict)
        open("/tmp/{0}.xml".format(app_dict['appName']),"w").write(doc)
        tmp = open('/tmp/{0}.xml'.format(app_dict['appName']),'rb').read()
        res = HttpResponse(tmp, mimetype="application/xml")
        res['Content-Disposition'] = 'attachment; filename={0}.xml'.format( 
                                      app_dict['appName'] )
        return res
    if request.method == 'GET' :
        return HttpResponse('<div>{0}</div>'.format(request.get_full_path()))

def gen_fake_app_dict():
    # This function will return a fake dictionary
    # to present the data.
    # This function is designed to verify app_description.xml
    return { 'appId':'1', 'appName':'fakeAppName', 'numOfSchemas':'1', 'schemas':[ { 'schemaId':'1', 'schemaName':'fakeSchema', 'numOfFields':'2', 'fields':[
     {'fieldId':'0', 'fieldName':'fakeIntFieldName', 
     'fieldRange':'10','numOfChoice':'0', 'choices':[], } ,  
     {'fieldId':'1', 'fieldName':'fakeChoiceName', 
     'fieldRange':'-2','numOfChoices':'3', 
     'choices':['choice one', 'choice two', 'choice three'], } , 
     ]}]}
    
