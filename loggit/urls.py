from django.conf.urls.defaults import *

urlpatterns = patterns('loggit.views.timeline_view',
    url(r'^timeline/index$', 'index', name='loggit_timeline_index'),
    url(r'^timeline/show$', 'show', name='loggit_timeline_show'),
)

urlpatterns += patterns('loggit.views.api.newdomain_view',
    url(r'^api/newdomain/index$', 'index', name='loggit_api_newdomain_index'),
    url(r'^api/newdomain/show$', 'show', name='loggit_api_newdomain_show'),
)

urlpatterns += patterns('loggit.views.newdomain_view',
    url(r'^newdomain/index$', 'index', name='loggit_newdomain_index'),
    url(r'^newdomain/show$', 'show', name='loggit_newdomain_show'),
)

urlpatterns += patterns('loggit.views.newdomain_analysis_view',
    url(r'^newdomain/analysis/index$', 'index', name='loggit_newdomain_analysis_index'),
)
