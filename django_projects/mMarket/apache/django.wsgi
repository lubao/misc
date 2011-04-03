import os
import sys
sys.path.append('/home/paul/django_projects')
sys.path.append('/home/paul/django-trunk/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mMarket.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

