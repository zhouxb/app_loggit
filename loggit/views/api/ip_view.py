# -*- coding:utf8 -*-

import datetime
from django.core.cache import cache
from annoying.decorators import ajax_request
from loggit.models.ip import Minutely
from loggit.conf import settings

@ajax_request
def index(request):
    start = request.GET.get('starttime', None)
    end = request.GET.get('endtime',None)
    name_list = request.GET.get('namelist','B')
    timeout = settings.LOGGIT_TIMEOUT
    page = request.GET.get('page', None)
    if page is None:
        page = 0
    else:
        page = int(page)
    num = 100
    if start and end :
        if start >= end :
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d')
            if cache.get(end+'ip') is None:
                domains = list(Minutely.objects(date__startswith=end).order_by('-count').values_list('ip', 'count','isp','province','date',)[num*page:num*(1+page)])
                cache.set(end+'ip', domains, timeout)
            else:
                domains = cache.get(end+'ip')
            total = Minutely.objects(date__startswith=end).count()
        else :
            start = datetime.datetime.strptime(start,'%Y-%m-%d').strftime('%Y%m%d0000')
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d0000')
            if cache.get(start+end+'ip') is None:
                domains = list(Minutely.objects(date__gte=start, date__lte=end).order_by('-count').values_list('ip', 'count','isp','province','date',)[num*page:num*(1+page)])
                cache.set(start+end+'ip', domains, timeout)
            else:
                domains = cache.get(start+end+'ip')
            total = Minutely.objects(date__gte=start, date__lte=end).count()
    return {'domains':domains, 'total':total}
