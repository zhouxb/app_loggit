import datetime
from django.core.cache import cache
from annoying.decorators import ajax_request
from loggit.models.newdomain import Minutely
from loggit.conf import settings

@ajax_request
def index(request):
    day = request.GET.get('day', None)
    page = request.GET.get('page', None)

    timeout = settings.LOGGIT_TIMEOUT if day is None else 60
    day = day or datetime.date.today().strftime('%Y%m%d')
    #day = '20120827'

    if cache.get(day) is None:
        domains = list(Minutely.objects(date__startswith=day).values_list('domain', ))
        cache.set(day, domains, timeout)

    domains = cache.get(day)
    total = len(domains)

    #FIXME
    if page is None:
        return {'domains':domains, 'total':total}

    page = int(page)
    num = 100
    if num*page > total:
        domains = []
    else:
        domains = domains[num*page:num*(1+page)]

    return {'domains':domains, 'total':total}

@ajax_request
def show(request):
    starttime = request.GET.get('starttime', None)
    endtime = request.GET.get('endtime', None)
    page = request.GET.get('page', None)

    if starttime is None and endtime is None:
        return {'domains':[]}

    k = '%s_%s' % (starttime, endtime)
    if cache.get(k) is None:
        if starttime is None:
            domains = list(Minutely.objects(date__lte=endtime).values_list('domain', ))
        elif endtime is None:
            domains = list(Minutely.objects(date__gte=starttime).values_list('domain', ))
        else:
            domains = list(Minutely.objects(date__gte=starttime, date__lte=endtime).values_list('domain', ))
        cache.set(k, domains, settings.LOGGIT_TIMEOUT)
    domains = cache.get(k)
    total = len(domains)

    #FIXME
    if page is None:
        return {'domains':domains, 'total':total}

    page = int(page)
    num = 100
    if num*page > total:
        domains = []
    else:
        domains = domains[num*page:num*(1+page)]

    return {'domains':domains, 'total':total}

