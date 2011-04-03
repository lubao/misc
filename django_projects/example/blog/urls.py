from django.conf.urls.defaults import *

urlpatterns = patterns('example.blog.views',
    (r'^add_comment/(\d+)/$', 'add_comment'),
    (r'(\d+)/$','post'),
	(r'', 'main'),
)
