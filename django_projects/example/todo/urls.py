from django.conf.urls.defaults import *
from todo.models import Item

urlpatterns = patterns('',
	(r'^mark_done/(\d*)/$', 'todo.views.mark_done'),
)
