# -*- coding:utf8 -*-
import datetime
import time
from django.core.cache import cache
from annoying.decorators import ajax_request
from loggit.models.domain import Minutely
from loggit.models.quality import Minutely as quality_mint
from loggit.conf import settings

@ajax_request
def index(request):
    start = request.GET.get('starttime', None)
    end = request.GET.get('endtime',None)
    timeout = settings.LOGGIT_TIMEOUT

    if start and end :
        if start >= end :
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d')
            if cache.get(end+'domain') is None:
                domains = list(Minutely.objects(date__startswith=end).order_by('-count').values_list('domain', 'count','isp','province','namelist','date',)[0:100])
                cache.set(end+'domain', domains, timeout)
            else:
                domains = cache.get(end+'domain')
        else :
            start = datetime.datetime.strptime(start,'%Y-%m-%d').strftime('%Y%m%d0000')
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d0000')
            if cache.get(start+end+'domain') is None:
                domains = list(Minutely.objects(date__gte=start, date__lte=end).order_by('-count').values_list('domain', 'count','isp','province','namelist','date',)[0:100])
                cache.set(start+end+'domain', domains, timeout)
            else:
                domains = cache.get(start+end+'domain')

    '''day = request.GET.get('day', None)
    page = request.GET.get('page', None)

    timeout = settings.LOGGIT_TIMEOUT if day is None else 60
    day = day or datetime.date.today().strftime('%Y%m%d')
    if page is None:
        page = 0
    else:
        page = int(page)
    num = 100
    total = Minutely.objects(date__startswith=day).count()

    if cache.get(day+'domain') is None:
        if num*page > total:
            domains = []
        else:
            domains = list(Minutely.objects(date__startswith=day).order_by('-count').values_list('domain', 'count','isp','province','namelist','date',)[num*page:num*(1+page)])
        cache.set(day+'domain', domains, timeout)
    else:
        domains = cache.get(day+'domain')
    #cache.set(day+'domain', domains, 1)
    #FIXME
    if page is None:
        return {'domains':domains, 'total':total}'''
    return {'domains':domains, 'total':100}

@ajax_request
def name_list(request):
    start = request.GET.get('starttime', None)
    end = request.GET.get('endtime',None)
    name_list = request.GET.get('namelist','B')
    timeout = settings.LOGGIT_TIMEOUT
    if start and end :
        if start >= end :
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d')
            if cache.get(end+'domain'+name_list) is None:
                domains = list(Minutely.objects(date__startswith=end,namelist=name_list).order_by('-count').values_list('domain', 'count','isp','province','namelist','date',)[0:100])
                cache.set(end+'domain'+name_list, domains, timeout)
            else:
                domains = cache.get(end+'domain'+name_list)
        else :
            start = datetime.datetime.strptime(start,'%Y-%m-%d').strftime('%Y%m%d0000')
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d0000')
            if cache.get(start+end+'domain'+name_list) is None:
                domains = list(Minutely.objects(date__gte=start, date__lte=end,namelist=name_list).order_by('-count').values_list('domain', 'count','isp','province','namelist','date',)[0:100])
                cache.set(start+end+'domain'+name_list, domains, timeout)
            else:
                domains = cache.get(start+end+'domain'+name_list)
    return {'domains':domains, 'total':100}

def map_percent(data):
    domain = data[0]
    count = data[1]
    isp = data[2]
    province = data[3]
    namelist = data[4]
    date = data[5]
    qm = quality_mint.objects(isp=isp,province=province,date=date).values_list('total',)
    if len(qm) != 0:
        strpre = "%0.2f" % (float(count)/float(qm[0])*100) + '%' 
    else:
        strpre ='0.0%'
    tuple_data = (domain,count,isp,province,namelist,date,strpre)
    return tuple_data

@ajax_request
def name_list_percent(request):
    start = request.GET.get('starttime', None)
    end = request.GET.get('endtime',None)
    name_list = request.GET.get('namelist','B')
    timeout = settings.LOGGIT_TIMEOUT
    if start and end :
        if start >= end :
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d')
            if cache.get(end+'domain'+name_list+'percent') is None:
                domains = Minutely.objects(date__startswith=end,namelist=name_list).order_by('-count').values_list('domain', 'count','isp','province','namelist','date',)[0:100]
                domains = map(map_percent,domains)
            else:
                domains = cache.get(end+'domain'+name_list+'percent')
        else :
            start = datetime.datetime.strptime(start,'%Y-%m-%d').strftime('%Y%m%d0000')
            end = datetime.datetime.strptime(end,'%Y-%m-%d').strftime('%Y%m%d0000')
            if cache.get(start+end+'domain'+name_list+'percent') is None:
                domains = Minutely.objects(date__gte=start, date__lte=end,namelist=name_list).order_by('-count').values_list('domain', 'count','isp','province','namelist','date',)[0:100]
                domains = map(map_percent,domains)
            else:
                domains = cache.get(start+end+'domain'+name_list+'percent')
    
    if len(start.split('-'))>0:
        cache.set(end+'domain'+name_list+'percent', domains, timeout)
    else:
        cache.set(start+end+'domain'+name_list+'percent', domains, timeout)
    return {'domains':domains, 'total':100}

@ajax_request
def alarm(request):
    starttime = request.GET.get('starttime',None)
    endtime = request.GET.get('endtime',None)

    timeout = settings.LOGGIT_TIMEOUT

    if starttime and endtime:
        if starttime >= endtime:
            day = datetime.datetime.now().strftime('%Y%m%d%H')
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

