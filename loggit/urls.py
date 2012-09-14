from django.conf.urls.defaults import *

urlpatterns = patterns('loggit.views.api.newdomain_view',
    url(r'^api/newdomain/index$', 'index', name='loggit_api_newdomain_index'),
    url(r'^api/newdomain/show$', 'show', name='loggit_api_newdomain_show'),
)

urlpatterns += patterns('loggit.views',
    url(r'^newdomain$', 'newdomain', name='loggit_newdomain'),
)
