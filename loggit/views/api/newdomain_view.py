import re
import datetime
from django.core.cache import cache
from annoying.decorators import ajax_request
from loggit.models.newdomain import Minutely, Filter
from loggit.conf import settings

@ajax_request
def index(request):
    day = request.GET.get('day', None)
    page = request.GET.get('page', None)

    day = day or datetime.date.today().strftime('%Y%m%d')
    domains = Minutely.by_day(day, day)

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
    domains = Minutely.by_day(starttime, endtime)

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

