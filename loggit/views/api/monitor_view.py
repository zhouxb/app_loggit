# -*- coding:utf8 -*-
import datetime
import time
from django.core.cache import cache
from annoying.decorators import ajax_request
from loggit.models.quality import Minutely as quality_mint
from loggit.conf import settings

@ajax_request
def index(request):
    starttime = request.GET.get('starttime',None)
    endtime = request.GET.get('endtime',None)

    timeout = settings.LOGGIT_TIMEOUT

    if starttime and endtime:
        if starttime >= endtime:
            day = datetime.datetime.strptime(endtime,'%Y-%m-%d').strftime('%Y%m%d')
            if cache.get(day+'alarm'+'success') is None:
                domains = list(quality_mint.objects(date__startswith=day).order_by('date'))
                success_data,failure_data,total_data = chart_total_data(domains)
                cache.set(day+'alarm'+'success', success_data, timeout)
                cache.set(day+'alarm'+'failure', failure_data, timeout)
                cache.set(day+'alarm'+'total', total_data, timeout)
            else:
                success_data = cache.get(day+'alarm'+'success')
                failure_data = cache.get(day+'alarm'+'failure')
                total_data = cache.get(day+'alarm'+'total')
        else:
            start = datetime.datetime.strptime(starttime,'%Y-%m-%d').strftime('%Y%m%d0000')
            end = datetime.datetime.strptime(endtime,'%Y-%m-%d').strftime('%Y%m%d0000')

            if cache.get(start+end+'alarm'+'success') is None:
                domains = list(quality_mint.objects(date__gte=start, date__lte=end).order_by('date'))
                success_data,failure_data,total_data = chart_total_data(domains)
                cache.set(start+end+'alarm'+'success', success_data, timeout)
                cache.set(start+end+'alarm'+'failure', failure_data, timeout)
                cache.set(start+end+'alarm'+'total', total_data, timeout)
            else:
                success_data = cache.get(start+end+'alarm'+'success')
                failure_data = cache.get(start+end+'alarm'+'failure')
                total_data = cache.get(start+end+'alarm'+'total')

    return {'success_data':success_data,'failure_data':failure_data,'total_data':total_data}


def chart_total_data(data):
    success_data = []
    fail_data = []
    total_data = []
    pre_date = ''
    success_count = 0
    fail_count = 0
    total_count = 0
    for k in data:
        if pre_date == k.date:
            success_count +=k.success
            fail_count +=k.failure
            total_count += k.total
        else:
            if pre_date:
                s=datetime.datetime(int(pre_date[0:4]),int(pre_date[4:6]),int(pre_date[6:8]),int(pre_date[8:10]),int(pre_date[10:12]),0)
                atime=time.mktime(s.timetuple())
                success_data.append({'x':atime*1000,'y':success_count})
                fail_data.append({'x':atime*1000,'y':fail_count})
                total_data.append({'x':atime*1000,'y':total_count})
            pre_date = k.date
            success_count = 0
            fail_count = 0
            total_count = 0
    return success_data,fail_data,total_data