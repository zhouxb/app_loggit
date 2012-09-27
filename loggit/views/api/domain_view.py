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


