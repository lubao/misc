from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^genConfig/', include('genConfig.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^genMyApp/showAppForm/$','genConfig.genApp.views.show_app_form'),
    (r'^genMyApp/genAppForm/$','genConfig.genApp.views.gen_app_form'),
    (r'^genMyForm/showOpForm/$','genConfig.genForm.views.show_op_form'),
    (r'^genMyForm/genOpForm/$','genConfig.genForm.views.gen_op_form'),
    (r'^sumSearch/search/$','genConfig.SumSearch.views.search_form'),
    (r'^sumSearch/result/$','genConfig.SumSearch.views.result_form'),
)
