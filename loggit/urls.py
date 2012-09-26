from django.conf.urls.defaults import *

urlpatterns = patterns('loggit.views.timeline_view',
    url(r'^timeline/index$', 'index', name='loggit_timeline_index'),
    url(r'^timeline/show$', 'show', name='loggit_timeline_show'),
)

urlpatterns += patterns('loggit.views.api.newdomain_view',
    url(r'^api/newdomain/index$', 'index', name='loggit_api_newdomain_index'),
    url(r'^api/newdomain/show$', 'show', name='loggit_api_newdomain_show'),
)

urlpatterns += patterns('loggit.views.newdomain.newdomain_view',
    url(r'^newdomain/index$', 'index', name='loggit_newdomain_index'),
    url(r'^newdomain/show$', 'show', name='loggit_newdomain_show'),
)

urlpatterns += patterns('loggit.views.newdomain.newdomain_analysis_view',
    url(r'^newdomain/analysis/index$', 'index', name='loggit_newdomain_analysis_index'),
)

urlpatterns += patterns('loggit.views.newdomain.newdomain_filter_view',
    url(r'^newdomain/filter/index$', 'index', name='loggit_newdomain_filter_index'),
    url(r'^newdomain/filter/create$', 'create', name='loggit_newdomain_filter_create'),
    url(r'^newdomain/filter/delete$', 'delete', name='loggit_newdomain_filter_delete'),
)

urlpatterns += patterns('loggit.views.api.domain_view',
    url(r'^api/domain/index$', 'index', name='loggit_api_domain_index'),
    url(r'^api/domain/name_list$', 'name_list', name='loggit_api_domain_name_list'),
    url(r'^api/domain/name_list_percent$', 'name_list_percent', name='loggit_api_domain_name_list_percent'),
    url(r'^api/domain/alarm$', 'alarm', name='loggit_api_domain_alarm'),
)

urlpatterns += patterns('loggit.views.domain.domain_view',
    url(r'^domain/index$', 'index', name='loggit_domain_index'),
    url(r'^domain_namelist/index$', 'namelist', name='loggit_domain_namelist_index'),
    url(r'^domain_namelistpercent/index$', 'namelistpercent', name='loggit_domain_namelistpercent_index'),
    url(r'^domain/alarm$', 'alarm', name='loggit_domain_alarm'),
)

urlpatterns += patterns('loggit.views.api.ip_view',
    url(r'^api/ip/index$', 'index', name='loggit_api_ip_index'),
)

urlpatterns += patterns('loggit.views.ip.ip_view',
    url(r'^ip/index$', 'index', name='loggit_ip_index'),
)

urlpatterns += patterns('loggit.views.api.leadingin_view',
    url(r'^api/leadingin/index$', 'index', name='loggit_api_leadingin_index'),
)

urlpatterns += patterns('loggit.views.leadingin.leadingin_view',
    url(r'^leadingin/index$', 'index', name='loggit_leadingin_index'),
)

urlpatterns += patterns('loggit.views.api.non80_view',
    url(r'^api/non80/index$', 'index', name='loggit_api_non80_index'),
)

urlpatterns += patterns('loggit.views.non80.non80_view',
    url(r'^non80/index$', 'index', name='loggit_non80_index'),
)
